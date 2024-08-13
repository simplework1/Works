import os
from PyPDF2 import PdfMerger

# Directory containing your PDF files
pdf_directory = '/path/to/your/pdfs'

# Helper function to extract numeric value from filename
def extract_number(filename):
    # Assuming the filename starts with the number (e.g., "1.pdf", "11.pdf")
    return int(''.join(filter(str.isdigit, filename)))

# Get a list of PDF files in the directory, sorted numerically by the number in the filename
pdf_files = sorted([f for f in os.listdir(pdf_directory) if f.endswith('.pdf')], key=extract_number)

# Initialize PdfMerger
merger = PdfMerger()

# Loop through all the PDF files and append them to the merger
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_directory, pdf_file)
    merger.append(pdf_path)

# Write out the combined PDF
output_path = os.path.join(pdf_directory, 'combined.pdf')
merger.write(output_path)
merger.close()

print(f"Combined PDF saved to {output_path}")
