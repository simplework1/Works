from docx import Document
from docx.shared import Inches

# Load the DOCX file
doc = Document("/mnt/data/file-5W8eQY6g2eRPjh0ZayYgiIpj")

# Define margins for the entire document
for section in doc.sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

# Save the modified document
doc.save("document_with_set_margins.docx")
