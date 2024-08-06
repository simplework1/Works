import asyncio
from pyppeteer import launch

async def html_to_pdf(html_file_path, output_pdf_path):
    browser = await launch()
    page = await browser.newPage()
    
    # Read the HTML file content
    with open(html_file_path, 'r') as file:
        html_content = file.read()

    # Set the content of the page
    await page.setContent(html_content)
    
    # Define PDF options including margins and background
    pdf_options = {
        'path': output_pdf_path,
        'format': 'A4',
        'printBackground': True,
        'margin': {
            'top': '0.5in',
            'right': '0.5in',
            'bottom': '0.5in',
            'left': '0.5in'
        }
    }
    
    # Generate PDF
    await page.pdf(pdf_options)
    await browser.close()

html_file_path = '/mnt/data/file-E3uDzrwnJsTPIHbHQZspGb3O'  # Path to the HTML file
output_pdf_path = '/mnt/data/output.pdf'  # Path to save the output PDF

asyncio.get_event_loop().run_until_complete(html_to_pdf(html_file_path, output_pdf_path))

print(f'PDF file has been created at {output_pdf_path}')
