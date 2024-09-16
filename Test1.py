import requests

def search_duckduckgo(query):
    url = 'https://api.duckduckgo.com/'
    params = {
        'q': query,  # Your search query
        'format': 'json',  # Output format
        'pretty': 1  # For more readable JSON
    }
    response = requests.get(url, params=params)
    return response.json()

query = "python news 2023"  # Include a date-related term in your query
results = search_duckduckgo(query)
print(results)
