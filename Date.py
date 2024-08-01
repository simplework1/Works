from datetime import datetime

# Given date string
date_str = "20240715"

# Convert the string to a datetime object
date_obj = datetime.strptime(date_str, "%Y%m%d")

# Format the datetime object to the desired format
formatted_date = date_obj.strftime("%dth %b, %Y")

print(formatted_date)
