from docx import Document

# Load the DOCX file
doc = Document("your_document.docx")

# Variables to track the start and end of the range
in_sanctions_section = False
tables_to_delete = []

# Loop through all elements in the document
for i, element in enumerate(doc.element.body):
    # Check if the element is a paragraph with the style 'Heading 1', 'Heading 2', etc.
    if hasattr(element, 'text'):
        paragraph = doc.paragraphs[i]
        if paragraph.style.name.startswith('Heading'):
            if 'Sanctions' in paragraph.text:
                in_sanctions_section = True  # Start tracking
            elif 'Adverse Press' in paragraph.text:
                in_sanctions_section = False  # Stop tracking

    # If in the Sanctions section and the element is a table, mark it for deletion
    if in_sanctions_section and element.tag.endswith('tbl'):
        tables_to_delete.append(element)

# Remove the tables marked for deletion
for table in tables_to_delete:
    doc.element.body.remove(table)

# Save the modified document
doc.save("modified_document.docx")
