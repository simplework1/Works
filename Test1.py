from docx import Document
from docx.shared import Pt

def is_blank_paragraph(paragraph):
    """
    Check if a paragraph is effectively blank.
    """
    if not paragraph.text.strip() and not paragraph.runs:
        return True
    if all(run.text.strip() == '' for run in paragraph.runs):
        return True
    return False

def remove_blank_pages(doc):
    """
    Remove paragraphs that might be causing blank pages.
    """
    # Identify and remove blank paragraphs
    for para in doc.paragraphs:
        if is_blank_paragraph(para):
            p = para._element
            p.getparent().remove(p)
    
    # You can add more logic here if you identify other causes of blank pages, 
    # such as manual page breaks or section breaks.
    
    return doc

# Load your document
doc = Document('input_document.docx')

# Remove blank pages
doc = remove_blank_pages(doc)

# Save the cleaned document
doc.save('cleaned_document.docx')
