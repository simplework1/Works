import pdfplumber
from docx import Document
from docx.shared import Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import nsdecls

# Function to set table grid (borders)
def set_table_borders(table):
    tbl = table._tbl  # Get the table's underlying XML element
    tblPr = tbl.tblPr  # Table properties

    # Create a table border element
    tblBorders = OxmlElement('w:tblBorders')
    for border_name in ["top", "left", "bottom", "right", "insideH", "insideV"]:
        border = OxmlElement(f'w:{border_name}')
        border.set('w:val', 'single')
        border.set('w:sz', '4')  # Border size (can adjust as needed)
        border.set('w:space', '0')
        border.set('w:color', '000000')  # Black color for the borders
        tblBorders.append(border)

    tblPr.append(tblBorders)  # Add the border element to table properties

# Function to extract tables from a PDF and save them to a DOCX file with grid borders
def pdf_table_to_docx(pdf_file_path, docx_file_path):
    # Open the PDF file
    with pdfplumber.open(pdf_file_path) as pdf:
        # Create a new Document
        doc = Document()

        for i, page in enumerate(pdf.pages):
            # Extract tables from the page
            tables = page.extract_tables()

            if tables:
                for table in tables:
                    doc.add_paragraph(f"Table from Page {i + 1}")
                    doc_table = doc.add_table(rows=1, cols=len(table[0]))

                    # Add header row
                    hdr_cells = doc_table.rows[0].cells
                    for j, cell_value in enumerate(table[0]):
                        hdr_cells[j].text = str(cell_value)

                    # Add the rest of the rows
                    for row_data in table[1:]:
                        row_cells = doc_table.add_row().cells
                        for j, cell_value in enumerate(row_data):
                            row_cells[j].text = str(cell_value)

                    # Apply table grid/borders
                    set_table_borders(doc_table)

                doc.add_page_break()

            else:
                doc.add_paragraph(f"No tables found on Page {i + 1}")
                doc.add_page_break()

        # Save the DOCX file
        doc.save(docx_file_path)

# Paths to the input PDF and output DOCX
pdf_file_path = "/mnt/data/file-9dogRF3PTZ5f3bxbnvf4DDfQ"
docx_file_path = "/mnt/data/output_with_grid.docx"

# Convert PDF tables to DOCX with table grid
pdf_table_to_docx(pdf_file_path, docx_file_path)
