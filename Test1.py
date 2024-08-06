import asyncio
from pyppeteer import launch

async def generate_pdf(html_content, pdf_path):
    browser = await launch(headless=True, executablePath=r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    page = await browser.newPage()
    
    await page.setContent(html_content)
    
    # Wait for content to load
    await page.waitForSelector('body')
    
    # Get the height of the rendered content
    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.scrollWidth,
            height: document.documentElement.scrollHeight,
            deviceScaleFactor: window.devicePixelRatio
        }
    }''')
    
    # Set the viewport to the height of the content
    await page.setViewport({
        'width': dimensions['width'],
        'height': dimensions['height'],
        'deviceScaleFactor': dimensions['deviceScaleFactor']
    })
    
    # Adjust the page.pdf settings to capture the entire scrollable content
    await page.pdf({
        'path': pdf_path,
        'printBackground': True,  # Enable background graphics
        'width': f"{dimensions['width']}px",
        'height': f"{dimensions['height']}px",
        'margin': {
            'top': '1in',
            'right': '0.5in',
            'bottom': '1in',
            'left': '0.5in'
        },
        'scale': 1  # Adjust the scale as needed
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
    <p>Content goes here...</p>
    <p>More content...</p>
    <p>Even more content...</p>
    <p>Even more content...</p>
    <p>Even more content...</p>
    <p>Even more content...</p>
    <p>Even more content...</p>
    <p>Even more content...</p>
    <p>Even more content...</p>
    <p>Even more content...</p>
    <p>Even more content...</p>
    <p>Even more content...</p>
    <p>Even more content...</p>
    <p>Even more content...</p>
    <p>Even more content...</p>
    <p>Even more content...</p>
    <p>Even more content...</p>
    <p>Even more content...</p>
    <p>Even more content...</p>
    <p>Even more content...</p>
    <p>Even more content...</p>
</body>
</html>
"""
pdf_path = 'output.pdf'

# Running the function
asyncio.get_event_loop().run_until_complete(generate_pdf(html_content, pdf_path))
