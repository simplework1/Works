from bs4 import BeautifulSoup

# Function to parse the table and store rows as a list of lists
def parse_html_table(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    # Locate the table under the "Sanctions" heading
    table = soup.find('h3', text="Sanctions").find_next('table')
    
    # Initialize list to store rows
    table_data = []

    # Iterate over each row in the table body
    for row in table.find_all('tr'):
        row_data = []
        # Iterate over each cell in the row
        for cell in row.find_all(['td', 'th']):
            # Check if the cell has multiple lines (e.g., <ul><li>...</li></ul>)
            if cell.find('ul'):
                # Extract the list items and store them as a nested list
                multiline_data = [li.get_text(strip=True) for li in cell.find_all('li')]
                row_data.append(multiline_data)
            else:
                # Otherwise, just get the text content
                row_data.append(cell.get_text(strip=True))
        
        # Append the row data to the table data list
        table_data.append(row_data)

    return table_data

# Path to your HTML file
html_file_path = "/mnt/data/file-2G2fOAW3oJ8yAjW42RUYAzHJ"

# Parse the table and store the data
table_data = parse_html_table(html_file_path)

# Output the parsed data
for row in table_data:
    print(row)
