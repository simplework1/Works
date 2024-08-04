# Sample list of strings
strings_list = ["apple", "banana", "cherry", "date"]

# Convert each string to be enclosed in double quotes
quoted_list = [f'"{s}"' for s in strings_list]

# Print the list as a string with double quotes
print(f"[{', '.join(quoted_list)}]")
