import os
from docx import Document
from docxcompose.composer import Composer

# Directory where your Word files are stored
directory = "/path/to/your/word/files"

# Get a list of all Word files in the directory
files = [f for f in os.listdir(directory) if f.endswith('.docx')]

# Sort the files by their numerical order
files.sort(key=lambda x: int(os.path.splitext(x)[0]))

# Create a new Document to start merging
merged_doc = Document()

# Initialize Composer with the base document
composer = Composer(merged_doc)

# Loop through each file and append its content to the merged document
for i, file in enumerate(files):
    file_path = os.path.join(directory, file)
    sub_doc = Document(file_path)
    
    if i > 0:  # Add a page break before appending the next document
        merged_doc.add_page_break()
    
    composer.append(sub_doc)

# Save the merged document
output_path = os.path.join(directory, "merged_document_with_page_breaks.docx")
composer.save(output_path)

print("All documents have been merged successfully with page breaks.")
