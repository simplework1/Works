from docx import Document
from docx.shared import Cm
from docx.enum.table import WD_ROW_HEIGHT_RULE

# Load the existing document
doc = Document('input.docx')  # Replace with your document's path

# Define the desired row height (e.g., 2 centimeters)
desired_height = Cm(2)

# Iterate through all tables in the document
for table in doc.tables:
    for row in table.rows:
        # Set the row height
        row.height = desired_height
        row.height_rule = WD_ROW_HEIGHT_RULE.EXACTLY

# Save the modified document
doc.save('output.docx')  # Replace with your desired output path
