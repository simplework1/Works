from docx import Document
from docx.shared import Inches

# Load your document
doc = Document('/mnt/data/file-zeFuBqvGaSyG19OZvYk7V4V2')

# The text of the heading where the paragraph and table should align
heading_text = "1.1 Background and Objective"  # Replace this with the exact heading text

# The paragraph you want to align the table with
paragraph_to_align_with = None
table_to_adjust = None

# Iterate through the paragraphs to find the heading
for i, paragraph in enumerate(doc.paragraphs):
    if heading_text in paragraph.text:
        # Found the heading paragraph, now find the next table
        paragraph_to_align_with = paragraph
        for j in range(i + 1, len(doc.paragraphs)):
            if doc.paragraphs[j]._element.tag.endswith('tbl'):
                table_to_adjust = doc.tables[0]  # Assuming the first table encountered needs adjustment
                break
        break

# Adjust the left indentation of the paragraph (for reference)
if paragraph_to_align_with:
    paragraph_indent = paragraph_to_align_with.paragraph_format.left_indent

# Adjust the left indentation of the table
if table_to_adjust:
    table_to_adjust._element.get_or_add_trPr().append(
        OxmlElement('w:tblInd')
    ).set(qn('w:w'), str(paragraph_indent))  # Set the table's indent to match the paragraph's indent

# Save the modified document
doc.save('/mnt/data/modified_document_with_adjusted_table_indent.docx')
