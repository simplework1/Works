from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def insert_section_break(document):
    # Insert a section break to start a new section
    sectPr = document.sections[-1]._sectPr  # get the last section
    pgMar = OxmlElement('w:sectPr')
    pgMar.set(qn('w:type'), 'nextPage')
    sectPr.append(pgMar)

def merge_documents(doc1_path, doc2_path, output_path):
    # Load the first document
    doc1 = Document(doc1_path)

    # Insert a section break to start the second document on a new section
    insert_section_break(doc1)

    # Load the second document
    doc2 = Document(doc2_path)

    # Append each paragraph and its elements to the first document
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
