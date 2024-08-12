from pdfminer.high_level import extract_pages
from pdfminer.layout import (
    LTTextBox, LTTextLine, LTChar, LTImage, LTRect, LTLine, LTAnno
)
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.section import WD_SECTION
from io import BytesIO
from PIL import Image

def add_image_to_doc(doc, image_data):
    image = Image.open(BytesIO(image_data))
    image_stream = BytesIO()
    image.save(image_stream, format="PNG")
    image_stream.seek(0)
    doc.add_picture(image_stream)

def add_table_to_doc(doc, table_data):
    rows = len(table_data)
    cols = max(len(row) for row in table_data)
    table = doc.add_table(rows=rows, cols=cols)
    for i, row in enumerate(table_data):
        for j, cell in enumerate(row):
            table.cell(i, j).text = cell
    # Add styling and formatting if necessary

def extract_font_color(char):
    """Extract the font color from an LTChar object."""
    color = char.graphicstate.ncs
    if isinstance(color, tuple) and len(color) >= 3:
        return RGBColor(int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))
    return None

# Path to your PDF
pdf_path = "your_pdf_file.pdf"

# Create a new Word document
doc = Document()

# Extract pages from PDF
for page_layout in extract_pages(pdf_path):
    table_data = []
    in_table = False
    for element in page_layout:
        if isinstance(element, LTTextBox):
            for line in element:
                if isinstance(line, LTTextLine):
                    # Identify if the text line is part of a table
                    if in_table or "Table" in line.get_text():
                        in_table = True
                        row_data = []
                        for char in line:
                            if isinstance(char, LTChar):
                                row_data.append(char.get_text())
                        table_data.append(row_data)
                    else:
                        # Create a new paragraph in the Word document
                        paragraph = doc.add_paragraph()
                        for char in line:
                            if isinstance(char, LTChar):
                                run = paragraph.add_run(char.get_text())
                                run.font.size = Pt(char.size)
                                if 'Bold' in char.fontname:
                                    run.bold = True
                                if 'Italic' in char.fontname:
                                    run.italic = True
                                color = extract_font_color(char)
                                if color:
                                    run.font.color.rgb = color
                        if line.get_x() > 100:
                            paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                        elif line.get_x() < 100:
                            paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
                        else:
                            paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
        
        elif isinstance(element, LTRect):
            # If we encounter a rectangle, it might signify a table boundary
            in_table = True

        elif isinstance(element, LTLine):
            # Horizontal lines can also indicate table rows
            in_table = True

        elif isinstance(element, LTImage):
            add_image_to_doc(doc, element.stream.get_data())
        
        # Detect end of table
        if in_table and isinstance(element, LTAnno) and element.get_text() == "\n":
            in_table = False
            if table_data:
                add_table_to_doc(doc, table_data)
                table_data = []

    # Add a page break after each page to mimic PDF layout
    doc.add_section(WD_SECTION.NEW_PAGE)

# Save the Word document
doc.save("output_with_tables.docx")
