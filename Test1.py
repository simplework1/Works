from docx import Document
from docx.shared import Pt

# Load the DOCX file
doc = Document("/mnt/data/file-hi8SbR8eCb763w48a73Sdt4R")

# Your table data
table_data = [
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
    # Insert a new table with the correct number of rows and columns
    table = doc.add_table(rows=0, cols=len(table_data[0]))

    # Add the header row
    hdr_cells = table.add_row().cells
    for i, hdr_text in enumerate(table_data[0]):
        hdr_cells[i].text = hdr_text

    # Add the rest of the rows
    for row_data in table_data[1:]:
        row_cells = table.add_row().cells
        for i, cell_data in enumerate(row_data):
            if isinstance(cell_data, list):
                # Handle multiline cells
                cell_text = '\n'.join(cell_data)
            else:
                cell_text = str(cell_data)
            row_cells[i].text = cell_text

            # Apply some basic formatting
            for paragraph in row_cells[i].paragraphs:
                paragraph.style = doc.styles['Normal']
                paragraph_format = paragraph.paragraph_format
                paragraph_format.space_after = Pt(0)

    # Move the table to be right after the "Sanctions" paragraph
    sanctions_paragraph._element.addnext(table._element)

else:
    print("Sanctions heading not found in the document.")

# Save the modified document
doc.save("modified_document_with_table.docx")
