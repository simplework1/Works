from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def generate_pdf_from_html(html_content: str, pdf_path: str, chrome_path: str):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--print-to-pdf=' + pdf_path)  # Print to PDF
    
    # Specify the path to the Chrome executable if needed
    chrome_options.binary_location = chrome_path

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    # Create a temporary HTML file to load in the browser
    with open("temp.html", "w") as file:
        file.write(html_content)

    # Load the HTML file in the browser
    driver.get("file://" + os.path.abspath("temp.html"))

    # Give the browser time to load content
    time.sleep(2)

    # Print the page as a PDF
    driver.execute_script('window.print();')

    # Close the browser
    driver.quit()

# Example usage
html_content = """
<html>
<body>
    <h1>Hello, World!</h1>
    <p>This is a PDF generated from HTML content using Selenium.</p>
</body>
</html>
"""

pdf_path = "output.pdf"
chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Update this path if necessary

generate_pdf_from_html(html_content, pdf_path, chrome_path)
