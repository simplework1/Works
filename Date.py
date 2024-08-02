from datetime import datetime

# Current date and time
now = datetime.now()

# Format the date and time
formatted_date = now.strftime("%d{S} %B, %Y %I:%M %p")

# Function to get the appropriate suffix for day of the month
def get_day_suffix(day):
    return 'th' if 11<=day<=13 else {1:'st', 2:'nd', 3:'rd'}.get(day%10, 'th')

# Replace placeholder with the correct suffix
day = now.day
formatted_date = formatted_date.replace("{S}", get_day_suffix(day))

print(formatted_date)
