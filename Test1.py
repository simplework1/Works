from docx import Document
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml
from docx.shared import Pt

# Load the DOCX file
doc = Document("/mnt/data/file-hi8SbR8eCb763w48a73Sdt4R")

# Your table data
table_data = [
    # Example data
    ['aliases', 'dob', 'name', 'otherInfo', 'sanctions', 'source'],
    [["A.K.A. KHORASAN SPACE AGENCY", "A.K.A. NPFWD"], '10/12/1985', 'Name Example', 'Other Info Example', ["IFSR", "NPWMD"], 'OFAC'],
    # Add more rows as needed
]

# Locate the "Sanctions" heading
sanctions_paragraph = None
for para in doc.paragraphs:
    if 'Sanctions' in para.text:
        sanctions_paragraph = para
        break

if sanctions_paragraph:
    # Insert a new table after the "Sanctions" heading
    table = doc.add_table(rows=1, cols=len(table_data[0]))
    hdr_cells = table.rows[0].cells

    # Fill in the header row
    for i, hdr_text in enumerate(table_data[0]):
        hdr_cells[i].text = hdr_text

    # Add the rest of the rows
    for row_data in table_data[1:]:
        row_cells = table.add_row().cells
        for i, cell_data in enumerate(row_data):
            if isinstance(cell_data, list):
                # Handle multiline cells
                row_cells[i].text = '\n'.join(cell_data)
            else:
                row_cells[i].text = str(cell_data)
    
    # Apply formatting to make multiline cells render correctly
    for row in table.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                paragraph.style = doc.styles['Normal']
                paragraph_format = paragraph.paragraph_format
                paragraph_format.space_after = Pt(0)
else:
    print("Sanctions heading not found in the document.")

# Save the modified document
doc.save("modified_document_with_table.docx")
