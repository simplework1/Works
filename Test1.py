from docx import Document
from docx.shared import Pt

# Load your document
doc = Document("/mnt/data/file-bhnUIPWXzxZdiMv1vOhtoNWz")  # Use your file path here

# Remove extra white spaces for all paragraphs
for para in doc.paragraphs:
    para.paragraph_format.space_before = Pt(0)
    para.paragraph_format.space_after = Pt(0)

# Remove extra white spaces for all tables
for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                paragraph.paragraph_format.space_before = Pt(0)
                paragraph.paragraph_format.space_after = Pt(0)

# Save the modified document
doc.save("/mnt/data/modified_document_without_whitespace.docx")
