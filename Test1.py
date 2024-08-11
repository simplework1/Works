import pdfplumber
from docx import Document
from docx.table import Table

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

            doc.add_page_break()

        # Save the DOCX file
        doc.save(docx_file_path)

# Paths to the input PDF and output DOCX
pdf_file_path = "path_to_your_pdf.pdf"
docx_file_path = "output.docx"

# Convert PDF tables to DOCX
pdf_table_to_docx(pdf_file_path, docx_file_path)
