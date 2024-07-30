from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# Define the content dictionary
content_dict = {
    "Case Information": {
        "Background and Objective": (
            "According to the engagement letter dated 02 May 2017,  (\"Client\" or \"you\") "
            "has requested Deloitte Touche Tohmatsu India Limited Liability Partnership (\"DTTILLP\" or \"we\" or "
            "\"us\") to conduct Counterparty Due Diligence on the following Targets."
        ),
        "Table": [
            ["Target", "Alias", "Identifier"],
            ["Viva Clothing", "Varsha Mitesh Dave", "Varsha"],
            ["Visalakshi Sivaprakasam", "S Visalakshi", "Visalakshi"]
        ],
        "Methodology": (
            "The Counterparty Due Diligence consisted of online public record research, including searches covering "
            "corporate records and filings to identify company details, corporate structure and personal details; news "
            "media and trade sources to identify business profile, political / business affiliations and adverse publicity; "
            "litigation records where accessible; regulatory searches and sanctions screening; and other information "
            "search engines. Where possible, we broadened the scope of our online searches to include all relevant "
            "jurisdictions nationwide. Note that we focused primarily upon India."
        )
    }
}

# Create a new Document
doc = Document()

# Function to add a heading with a specific style
def add_heading_with_style(doc, text, level):
    heading = doc.add_heading(level=level)
    run = heading.add_run(text)
    run.font.size = Pt(14)  # Adjust size as needed
    run.bold = True
    return heading

# Function to add a table with specific data
def add_table(doc, data):
    table = doc.add_table(rows=len(data), cols=len(data[0]))
    table.style = 'Table Grid'
    for row_idx, row in enumerate(data):
        for col_idx, cell in enumerate(row):
            table.cell(row_idx, col_idx).text = cell

# Add content based on the dictionary
for main_title, sections in content_dict.items():
    # Add main title
    add_heading_with_style(doc, main_title, level=1)
    
    for sub_title, content in sections.items():
        # Add sub-title
        add_heading_with_style(doc, sub_title, level=2)
        
        # Add content (either text or table)
        if isinstance(content, str):
            doc.add_paragraph(content)
        elif isinstance(content, list):
            add_table(doc, content)

# Save the document
output_path = '/mnt/data/generated_document.docx'
doc.save(output_path)

print(f"Document saved to {output_path}")
