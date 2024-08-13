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
for file in files:
    file_path = os.path.join(directory, file)
    sub_doc = Document(file_path)
    composer.append(sub_doc)

# Save the merged document
output_path = os.path.join(directory, "merged_document.docx")
composer.save(output_path)

print("All documents have been merged successfully.")
