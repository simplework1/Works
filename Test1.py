from docx import Document

# Load the DOCX file
doc = Document("your_document.docx")

# Variables to track the start and end of the range
in_sanctions_section = False
tables_to_delete = []

# Loop through paragraphs to find the "Sanctions" and "Adverse Press" headings
for para in doc.paragraphs:
    if para.style.name.startswith('Heading'):
        if 'Sanctions' in para.text:
            in_sanctions_section = True
        elif 'Adverse Press' in para.text:
            in_sanctions_section = False

    # If we're in the Sanctions section and we find a table, mark it for deletion
    if in_sanctions_section:
        # Look ahead to the next elements to see if it's a table
        next_index = doc.paragraphs.index(para) + 1
        while next_index < len(doc.paragraphs) and doc.paragraphs[next_index].style.name != 'Heading 1':
            element = doc.element.body[next_index]
            if element.tag.endswith('tbl'):
                tables_to_delete.append(element)
            next_index += 1

# Remove the tables marked for deletion
for table in tables_to_delete:
    doc.element.body.remove(table)

# Save the modified document
doc.save("modified_document.docx")
