from docx import Document
from docx.shared import Inches
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# Load the DOCX file
doc = Document("/mnt/data/file-5W8eQY6g2eRPjh0ZayYgiIpj")

# Set the page size to A4 (21cm x 29.7cm)
section = doc.sections[0]
section.page_width = Inches(8.27)
section.page_height = Inches(11.69)

# Optional: Set the margins if needed
section.top_margin = Inches(1)
section.bottom_margin = Inches(1)
section.left_margin = Inches(1)
section.right_margin = Inches(1)

# Save the modified document
doc.save("document_set_to_A4.docx")
