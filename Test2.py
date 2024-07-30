from docx import Document
from docx.shared import Pt, RGBColor

# Load the document
doc_path = '/mnt/data/file-ElcTcoKfxzDZXUuigvU7uX32'
doc = Document(doc_path)

# Locate the table
table = doc.tables[0]  # assuming the table you want to edit is the first one

# Define the new details
new_details = {
    'Viva Clothing': 'New Firm Name',
    'Varsha Mitesh Dave': 'New Varsha Dave',
    'Visalakshi Sivaprakasam': 'New Visalakshi'
}

# New rows to be added
new_rows = [
    ['New Firm 1', 'Alias 1', 'Identifier 1'],
    ['New Firm 2', 'Alias 2', 'Identifier 2']
]

# Function to replace text while preserving formatting
def replace_text_in_cell(cell, new_text):
    for paragraph in cell.paragraphs:
        if paragraph.text.strip() in new_details:
            for run in paragraph.runs:
                run.text = new_text

# Function to add new row with the same format as the existing ones
def add_row_with_format(table, data):
    new_row = table.add_row()
    for i, cell in enumerate(new_row.cells):
        cell.text = data[i]
        # Copy formatting from the first row
        original_cell = table.rows[1].cells[i]  # Use the second row for format reference
        cell.paragraphs[0].style = original_cell.paragraphs[0].style
        cell.paragraphs[0].alignment = original_cell.paragraphs[0].alignment
        if len(original_cell.paragraphs[0].runs) > 0:
            original_run = original_cell.paragraphs[0].runs[0]
            new_run = cell.paragraphs[0].runs[0]
            new_run.bold = original_run.bold
            new_run.italic = original_run.italic
            new_run.underline = original_run.underline
            new_run.font.size = original_run.font.size
            new_run.font.color.rgb = original_run.font.color.rgb
            new_run.font.name = original_run.font.name

# Edit the table details
for row in table.rows:
    for cell in row.cells:
        cell_text = cell.text.strip()
        if cell_text in new_details:
            replace_text_in_cell(cell, new_details[cell_text])

# Add new rows
for data in new_rows:
    add_row_with_format(table, data)

# Save the document with changes
output_path = '/mnt/data/updated_document_with_new_rows_formatted.docx'
doc.save(output_path)

print(f"Document saved to {output_path}")
