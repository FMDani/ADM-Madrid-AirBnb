import pandas as pd
import numpy as np



listings = pd.read_csv('listings_detailed.csv', nrows=1125)
listings['price'] = pd.to_numeric(listings['price'].replace('[\$,]', '', regex=True), errors='coerce')
columns_to_keep = ['id', 'name', 'description', 'host_id', 'host_name','latitude', 'longitude', 'room_type', 'bathrooms', 'beds','price', 'number_of_reviews', 'last_review']  # Sostituisci con i nomi delle colonne che vuoi mantenere
listings = listings[columns_to_keep]

# Salva i risultati in un nuovo file CSV o utilizza il dataframe come necessario
listings.to_csv('listings.csv', index=False)


# Replace 'your_file.csv' with the actual path to your CSV file
file_path = 'listings.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

pd.set_option('display.max_columns', None)
# Display the first 5 rows of the DataFrame
print(df.head())
