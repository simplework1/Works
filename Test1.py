from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import base64
import urllib.parse

# Set up Chrome options
options = Options()
options.add_argument('--headless')  # Ensure GUI is off
options.add_argument('--disable-gpu')  # Disable GPU rendering

# Set up the ChromeDriver service
service = Service('/path/to/chromedriver')  # Update with your path to ChromeDriver

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Your HTML content as a string
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Test Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a test HTML page rendered directly from a string.</p>
</body>
</html>
"""

# Create a data URL for the HTML content
data_url = 'data:text/html;charset=utf-8,' + urllib.parse.quote(html_content)

# Load the HTML content directly using driver.get()
driver.get(data_url)

# Define the print to PDF settings
settings = {
    "paperWidth": 8.27,  # A4 paper width in inches
    "paperHeight": 11.69,  # A4 paper height in inches
    "printBackground": True  # Prints the background graphics
}

# Generate the PDF using the DevTools Protocol
result = driver.execute_cdp_cmd("Page.printToPDF", settings)

# Decode the base64 encoded PDF data
pdf_data = base64.b64decode(result['data'])

# Save the PDF
with open("output.pdf", "wb") as f:
    f.write(pdf_data)

# Close the browser
driver.quit()
