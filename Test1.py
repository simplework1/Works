import asyncio
from pyppeteer import launch
import time

async def generate_pdf(html_content, pdf_path):
    browser = await launch(headless=True, executablePath=r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    page = await browser.newPage()
    await page.setContent(html_content)
    
    await page.pdf({
        'path': pdf_path,
        'format': 'A4',
        'printBackground': True,  # Enable background graphics
        'scale': 1.5,  # Adjust the scale as needed
        'margin': {
            'top': '1in',
            'right': '0.5in',
            'bottom': '1in',
            'left': '0.5in'
        }
    })
    
    await browser.close()

# HTML content and path for the PDF
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Sample PDF</title>
</head>
<body>
    <h1>This is a sample PDF with margins and background enabled</h1>
</body>
</html>
"""
pdf_path = 'output.pdf'

# Running the function
asyncio.get_event_loop().run_until_complete(generate_pdf(html_content, pdf_path))
