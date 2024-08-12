from docx import Document
from docx.oxml.table import CT_Tbl

# Load the DOCX file
doc = Document("/mnt/data/file-qWf0dm88iSENA1XfXdMeKie3")

# Variables to track the start and end of the range
in_sanctions_section = False

# Iterate over the document elements directly
for element in doc.element.body:
    # Check if the element is a paragraph
    if isinstance(element, docx.oxml.CT_P):
        paragraph = element.text

        # Check for "Sanctions" and "Adverse Press" headings
        if 'Sanctions' in paragraph:
            in_sanctions_section = True
        elif 'Adverse Press' in paragraph:
            in_sanctions_section = False

    # Check if the element is a table and within the "Sanctions" section
    if in_sanctions_section and isinstance(element, CT_Tbl):
        doc.element.body.remove(element)

# Save the modified document
doc.save("modified_document.docx")
