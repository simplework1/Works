from docx import Document
from docx.shared import Inches
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

# Load your document
doc = Document('/mnt/data/file-zeFuBqvGaSyG19OZvYk7V4V2')

# The text of the heading where the paragraph and table should align
heading_text = "1.1 Background and Objective"  # Replace this with the exact heading text

# Iterate through the paragraphs to find the heading
for i, paragraph in enumerate(doc.paragraphs):
    if heading_text in paragraph.text:
        # Find the next table after this paragraph
        for j in range(i + 1, len(doc.paragraphs)):
            # Check if the next element is a table
            if doc.paragraphs[j]._element.tag.endswith('tbl'):
                table = doc.tables[0]  # Assuming it's the first table encountered
                # Set manual left indentation
                table_indent = Inches(0.5)  # Adjust this value as necessary
                
                tbl = table._element
                tblPr = tbl.tblPr
                tblInd = OxmlElement('w:tblInd')
                tblInd.set(qn('w:w'), str(int(table_indent * 1440)))  # Convert inches to twips
                tblInd.set(qn('w:type'), 'dxa')
                tblPr.append(tblInd)
                
                break
        break

# Save the modified document
doc.save('/mnt/data/modified_document_with_manual_table_indent.docx')
