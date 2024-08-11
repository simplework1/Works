import os
from docx import Document
from docxcompose.composer import Composer

def merge_docx_files(docx_dir, output_docx_path):
    # Get all docx files in the directory
    docx_files = [f for f in os.listdir(docx_dir) if f.endswith('.docx')]
    docx_files.sort()  # Optional: Sort files if you want to merge them in a specific order
    
    # Initialize the master document
    if not docx_files:
        print("No DOCX files found in the directory.")
        return
    
    master = Document(os.path.join(docx_dir, docx_files[0]))
    composer = Composer(master)
    
    # Iterate through the remaining docx files and append them to the master document
    for docx_file in docx_files[1:]:
        doc = Document(os.path.join(docx_dir, docx_file))
        composer.append(doc)
    
    # Save the merged document
    composer.save(output_docx_path)
    print(f"All DOCX files have been merged into {output_docx_path}")

# Example usage
docx_dir = '/path/to/docx/output/directory'  # Replace with the directory containing your DOCX files
output_docx_path = '/path/to/save/final/output.docx'  # Replace with the path where you want to save the final DOCX

merge_docx_files(docx_dir, output_docx_path)
