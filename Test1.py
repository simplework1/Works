from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up Chrome options
options = Options()
options.add_argument('--headless')  # Ensure GUI is off
options.add_argument('--disable-gpu')  # Disable GPU rendering

# Set up the ChromeDriver service
service = Service('/path/to/chromedriver')  # Update with your path to ChromeDriver

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Load the webpage
driver.get('https://www.example.com')  # Replace with your desired URL

# Define the print to PDF settings
settings = {
    "paperWidth": 8.27,  # A4 paper width in inches
    "paperHeight": 11.69,  # A4 paper height in inches
    "printBackground": True  # Prints the background graphics
}

# Generate the PDF using the DevTools Protocol
result = driver.execute_cdp_cmd("Page.printToPDF", settings)

# Save the PDF
with open("output.pdf", "wb") as f:
    f.write(bytes(result['data'], encoding='utf-8'))

# Close the browser
driver.quit()
