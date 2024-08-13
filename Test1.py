import docx
from html4docx import HtmlToDocx
from docx.shared import Pt

# Your HTML content as a string
html_content = '''
<html>
<head><title>Sample HTML</title></head>
<body>
    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>
    <table border="1">
        <tr>
            <th>Header 1</th>
            <th>Header 2</th>
        </tr>
        <tr>
            <td>Row 1, Cell 1</td>
            <td>Row 1, Cell 2</td>
        </tr>
        <tr>
            <td>Row 2, Cell 1</td>
            <td>Row 2, Cell 2</td>
        </tr>
    </table>
</body>
</html>
'''

# Create a new Word Document
doc = docx.Document()

# Initialize HtmlToDocx converter
html_to_docx = HtmlToDocx()

# Convert HTML content to DOCX and add it to the document
html_to_docx.add_html_to_document(html_content, doc)

# Reduce the font size for all paragraphs
for paragraph in doc.paragraphs:
    for run in paragraph.runs:
        run.font.size = Pt(10)  # Reduce the font size to 10 points

# Reduce the font size for all tables
for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.size = Pt(8)  # Reduce the font size to 8 points
    table.style = 'Table Grid'  # Apply the 'Table Grid' style

# Save the generated DOCX file
output_file = "output_single_page.docx"
doc.save(output_file)

print(f"Document saved as {output_file}")
