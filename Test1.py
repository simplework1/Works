import os
from PyPDF2 import PdfReader, PdfWriter
from pdf2docx import Converter

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

def convert_pdf_to_docx(pdf_dir, output_dir):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Convert each PDF in the directory to DOCX
    for pdf_file in os.listdir(pdf_dir):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(pdf_dir, pdf_file)
            docx_path = os.path.join(output_dir, pdf_file.replace('.pdf', '.docx'))
            
            # Convert the PDF to DOCX using pdf2docx
            cv = Converter(pdf_path)
            cv.convert(docx_path, start=0, end=None)
            cv.close()
            
            print(f"Converted {pdf_file} to {docx_path}")

# Example usage
input_pdf_path = '/mnt/data/file-T6Q3jukeP7MrpduRtPhihlO1'  # Replace with your actual PDF file path
pdf_output_dir = '/path/to/pdf/output/directory'  # Replace with your output directory for PDFs
docx_output_dir = '/path/to/docx/output/directory'  # Replace with your output directory for DOCX files

# Split the PDF into individual pages
split_pdf(input_pdf_path, pdf_output_dir)

# Convert the split PDF pages to DOCX files
convert_pdf_to_docx(pdf_output_dir, docx_output_dir)
