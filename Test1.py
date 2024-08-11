import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf_path, output_dir):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Read the input PDF
    with open(input_pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        
        # Iterate through each page and save it as a separate PDF
        for page_num in range(num_pages):
            pdf_writer = PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_num])
            
            # Construct the output PDF file path
            output_pdf_path = os.path.join(output_dir, f"page_{page_num + 1}.pdf")
            
            # Write the page to the output PDF
            with open(output_pdf_path, 'wb') as output_pdf_file:
                pdf_writer.write(output_pdf_file)
                
            print(f"Saved: {output_pdf_path}")

# Example usage
input_pdf_path = 'path/to/your/input.pdf'
output_dir = 'path/to/your/output/directory'

split_pdf(input_pdf_path, output_dir)
