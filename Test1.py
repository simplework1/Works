from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def insert_section_break(document):
    # Create a section break that starts a new section on the next page
    sectPr = document.sections[-1]._sectPr
    sectType = OxmlElement('w:type')
    sectType.set(qn('w:val'), 'nextPage')
    sectPr.append(sectType)

def merge_documents(doc1_path, doc2_path, output_path):
    # Load the first document
    doc1 = Document(doc1_path)

    # Insert a section break to start the second document on a new page
    insert_section_break(doc1)

    # Load the second document
    doc2 = Document(doc2_path)

    # Append each element from the second document to the first one
    for element in doc2.element.body:
        doc1.element.body.append(element)

    # Save the merged document
    doc1.save(output_path)

# File paths
doc1_path = 'first_document.docx'
doc2_path = 'second_document.docx'
output_path = 'merged_document.docx'

# Merge the documents
merge_documents(doc1_path, doc2_path, output_path)
