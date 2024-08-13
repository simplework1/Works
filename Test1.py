import os
import win32com.client

# Paths for the input PDF and output Word document
pdf_path = r"C:\path\to\your\input.pdf"
docx_path = r"C:\path\to\your\output.docx"

# Ensure the output directory exists
output_dir = os.path.dirname(docx_path)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create an instance of Word application
word = win32com.client.Dispatch("Word.Application")

# Set to False to make Word visible during the operation (for debugging)
word.Visible = False

# Open the PDF file in Word
doc = word.Documents.Open(pdf_path)

# Save the opened PDF as a Word document
doc.SaveAs(docx_path, FileFormat=16)  # 16 corresponds to the wdFormatDocumentDefault (docx format)

# Close the document and Word application
doc.Close()
word.Quit()

print(f"PDF converted to Word document and saved as '{docx_path}'")
