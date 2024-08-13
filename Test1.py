from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import nsdecls

# Load your document
doc = Document('/mnt/data/file-acBRTWV3Sx7NnwmqqgA7Q2Gf')

# Select the paragraph where you want to add the line (for example, the first paragraph)
paragraph = doc.paragraphs[0]

# Create a border element
p = paragraph._element
pPr = p.get_or_add_pPr()
borders = OxmlElement('w:pBdr')
pPr.append(borders)

# Define the border properties
bottom = OxmlElement('w:bottom')
bottom.set(nsdecls('w'), 'single')  # single line
bottom.set('w:sz', '12')  # Thickness (12 in half-points, so 6 points thick)
bottom.set('w:color', '000000')  # Black color
borders.append(bottom)

# Save the modified document
doc.save('/mnt/data/modified_document_with_line.docx')
