from docx import Document

# Load the document
doc_path = '/mnt/data/file-LXtPQWGfJ4BA0m80MAyNJbNk'
doc = Document(doc_path)

# Locate the table
table = doc.tables[0]  # assuming the table you want to edit is the first one

# Define the new details
new_details = {
    'Viva Clothing': 'New Firm Name',
    'Varsha Mitesh Dave': 'New Varsha Dave',
    'Visalakshi Sivaprakasam': 'New Visalakshi'
}

# Function to replace text while preserving formatting
def replace_text_in_cell(cell, new_text):
    for paragraph in cell.paragraphs:
        if paragraph.text.strip() in new_details:
            for run in paragraph.runs:
                run.text = new_text

# Edit the table details
for row in table.rows:
    for cell in row.cells:
        cell_text = cell.text.strip()
        if cell_text in new_details:
            replace_text_in_cell(cell, new_details[cell_text])

# Save the document with changes
output_path = '/mnt/data/updated_document_formatted.docx'
doc.save(output_path)

print(f"Document saved to {output_path}")
