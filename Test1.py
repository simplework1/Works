from docx import Document

# Load the DOCX file
doc = Document("/mnt/data/file-5W8eQY6g2eRPjh0ZayYgiIpj")

# Variables to track the start and end of the range
in_sanctions_section = False
elements_to_delete = []

# Iterate over the document elements directly
for para in doc.paragraphs:
    # Check if the paragraph contains the "Sanctions" heading
    if 'Sanctions' in para.text:
        in_sanctions_section = True
    elif 'Adverse Press' in para.text:
        in_sanctions_section = False

    # Mark elements for deletion after "Sanctions" and before "Adverse Press"
    if in_sanctions_section:
        elements_to_delete.append(para)

# Remove the marked elements
for element in elements_to_delete:
    element._element.getparent().remove(element._element)

# Save the modified document
doc.save("modified_document_after_sanctions.docx")
