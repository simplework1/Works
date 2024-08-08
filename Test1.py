import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup

async def html_to_pdf(html_content, output_pdf_path):
    browser = await launch(headless=False, executablePath=r'C:\Program Files\Google\Chrome\Application\chrome.exe')  # Adjust the path as needed
    page = await browser.newPage()

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

def modify_html_styles(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    div = soup.find('div')
    if div:
        div['style'] = 'width: 100vw; height: 100vh; overflow: auto;'
    return str(soup)

# Example HTML content received
html_content = '''
<!DOCTYPE html>
<html>
<head>
    <title>Sample PDF</title>
</head>
<body>
    <div style="width: 70%; height: 80vh; overflow: scroll;">
        <h1 contenteditable="false" style="text-align: center;">This is a test content</h1>
        <!-- Add your content here -->
    </div>
</body>
</html>
'''

# Modify the HTML styles
modified_html_content = modify_html_styles(html_content)

# Define the output PDF path
pdf_path = 'output.pdf'

# Running the function
asyncio.get_event_loop().run_until_complete(html_to_pdf(modified_html_content, pdf_path))

print(f'PDF file has been created at {pdf_path}')
