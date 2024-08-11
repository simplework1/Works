from docx import Document
import os

# Function to merge docx files
def merge_docx(files, output):
    merged_document = Document()

    for index, file in enumerate(files):
        sub_doc = Document(file)
        
        # Skip the first paragraph of all documents except the first one to avoid extra blank lines
        if index != 0:
            sub_doc_paragraphs = sub_doc.paragraphs[1:]
        else:
            sub_doc_paragraphs = sub_doc.paragraphs

        for paragraph in sub_doc_paragraphs:
            # Add the content of each file
            merged_document.add_paragraph(paragraph.text)

        # Add a page break after each document except the last one
        if index < len(files) - 1:
            merged_document.add_page_break()

    # Save the merged document
    merged_document.save(output)

# Directory containing the .docx files
directory = 'path_to_directory'

# List all .docx files in the directory
files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.docx')]

# Sort the files by name (optional, in case you want them in a specific order)
files.sort()

# Output file name
output_file = 'merged_document.docx'

# Merge the documents
merge_docx(files, output_file)

print(f'Merged {len(files)} documents into {output_file}')
