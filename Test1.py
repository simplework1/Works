import pandas as pd
from fuzzywuzzy import fuzz

# Sample DataFrame
data = {
    'title': [
        'The quick brown fox', 'The quick brown fox jumps over the lazy dog', 
        'A quick brown fox', 'The quick brown foxes', 
        'A lazy dog', 'The quick fox', 'Lazy dog and quick fox'
    ],
    'other_column': [1, 2, 3, 4, 5, 6, 7]
}
df = pd.DataFrame(data)

# Function to find and remove fuzzy duplicates
def remove_fuzzy_duplicates(df, column, threshold=80):
    indices_to_remove = set()
    titles = df[column].tolist()
    
    for i in range(len(titles)):
        if i in indices_to_remove:
            continue
        
        for j in range(i + 1, len(titles)):
            if j in indices_to_remove:
                continue
            
            if fuzz.ratio(titles[i], titles[j]) >= threshold:
                indices_to_remove.add(j)
    
    df_cleaned = df.drop(indices_to_remove).reset_index(drop=True)
    return df_cleaned

# Remove fuzzy duplicates
df_cleaned = remove_fuzzy_duplicates(df, 'title', threshold=80)

# Display the cleaned DataFrame
print(df_cleaned)
