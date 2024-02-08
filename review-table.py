import pandas as pd
import numpy as np

reviews_detail = pd.read_csv('reviews_detailed.csv', nrows=2500)

reviews_detail['score'] = np.random.randint(1, 100, size=len(reviews_detail))  # Genera numeri casuali tra 1 e 5

columns_to_keep = ['id', 'listing_id', 'date', 'reviewer_id', 'reviewer_name', 'comments', 'score']  # Sostituisci con i nomi delle colonne che vuoi mantenere
reviews_detail = reviews_detail[columns_to_keep]

# Salva i risultati in un nuovo file CSV o utilizza il dataframe come necessario
reviews_detail.to_csv('reviews.csv', index=False)


# Replace 'your_file.csv' with the actual path to your CSV file
file_path = 'reviews.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

pd.set_option('display.max_columns', None)
# Display the first 5 rows of the DataFrame
print(df.head())