from docx import Document
from docx.shared import Pt

def clean_document(doc):
    # Set table.autofit = False for all tables in the document
    for table in doc.tables:
        table.autofit = False

    # Remove extra blank paragraphs or unnecessary blank spaces
    def remove_empty_paragraphs(doc):
        for para in doc.paragraphs:
            # Check if the paragraph is empty or consists only of whitespace
            if not para.text.strip():
                # Remove the paragraph by clearing its content
                para.clear()

    # First, remove empty paragraphs
    remove_empty_paragraphs(doc)

    # Save the cleaned document (optional: if you want to overwrite the original doc)
    # doc.save('cleaned_document.docx')

    return doc

# Example usage
doc = Document('your_document.docx')
cleaned_doc = clean_document(doc)
cleaned_doc.save('cleaned_document.docx')
