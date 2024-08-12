from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox, LTTextLine, LTChar, LTImage, LTRect
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from io import BytesIO
from PIL import Image

def add_image_to_doc(doc, image_data):
    # Use PIL to open the image data
    image = Image.open(BytesIO(image_data))
    
    # Save the image to a temporary location and add to the document
    image_stream = BytesIO()
    image.save(image_stream, format="PNG")
    image_stream.seek(0)
    
    doc.add_picture(image_stream)

# Path to your PDF
pdf_path = "your_pdf_file.pdf"

# Create a new Word document
doc = Document()

# Extract pages from PDF
for page_layout in extract_pages(pdf_path):
    for element in page_layout:
        if isinstance(element, LTTextBox):
            for line in element:
                if isinstance(line, LTTextLine):
                    # Create a new paragraph in the Word document
                    paragraph = doc.add_paragraph()
                    
                    # Iterate over each character in the line
                    for char in line:
                        if isinstance(char, LTChar):
                            run = paragraph.add_run(char.get_text())
                            # Set font size
                            run.font.size = Pt(char.size)
                            # Set bold/italic based on PDF font info
                            if 'Bold' in char.fontname:
                                run.bold = True
                            if 'Italic' in char.fontname:
                                run.italic = True
                            # Set font color
                            color = char.ncs.fill
                            if color:
                                run.font.color.rgb = RGBColor(int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))
                    
                    # Align paragraph based on the position in the PDF
                    if line.get_x() > 100:  # Adjust this condition as needed
                        paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                    elif line.get_x() < 100:
                        paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
                    else:
                        paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

        elif isinstance(element, LTImage):
            # Extract and insert image
            add_image_to_doc(doc, element.stream.get_data())
        
        elif isinstance(element, LTRect):
            # Handle rectangles or lines as needed (e.g., borders, underlines)
            pass
    
    # Add a page break after each page to mimic PDF layout
    doc.add_section(WD_SECTION.NEW_PAGE)

# Save the Word document
doc.save("output.docx")
