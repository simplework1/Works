import pypandoc

# Function to convert HTML to DOCX using Pandoc
def html_to_docx(html_file_path, docx_file_path):
    # Convert HTML to DOCX using pypandoc
    output = pypandoc.convert_file(html_file_path, 'docx', format='html', outputfile=docx_file_path)
    print(f"Conversion complete: {docx_file_path}")

# Paths to the input HTML and output DOCX
html_file_path = "path_to_your_html_file.html"
docx_file_path = "output.docx"

# Convert HTML to DOCX
html_to_docx(html_file_path, docx_file_path)
