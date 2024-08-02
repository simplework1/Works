import re

# Sample string
text = 'My name is "Niladri Mullick".'

# Regular expression to find text within quotes
match = re.search(r'"([^"]*)"', text)

# Extract the matched text if found
if match:
    quoted_text = match.group(1)
else:
    quoted_text = None

print(quoted_text)
