import pandas as pd
import numpy as np

# Carica i dati dai file CSV
reviews_detail = pd.read_csv('reviews.csv')
listings = pd.read_csv('listings.csv')
users_data = pd.read_csv('users.csv')
# Esegui il join utilizzando le colonne "listing_id" e "id"
merged_data = pd.merge(reviews_detail, listings, left_on='listing_id', right_on='id', how='inner', suffixes=('_review', '_listing'))

# Aggiungi le colonne "booking_id", "number_of_nights" e "total_price"
merged_data['booking_id'] = range(1, len(merged_data) + 1)  # Crea una sequenza di id per le prenotazioni
merged_data['number_of_nights'] = np.random.randint(1, 6, size=len(merged_data))  # Genera numeri casuali tra 1 e 5
merged_data['date_check_in'] = pd.to_datetime(merged_data['date']) - pd.to_timedelta(merged_data['number_of_nights'], unit='D')  # Calcola la data di check-in
merged_data['date_check_out'] = pd.to_datetime(merged_data['date'])
merged_data['price'] = pd.to_numeric(merged_data['price'].replace('[\$,]', '', regex=True), errors='coerce')
merged_data['total_price'] = merged_data['price'] * merged_data['number_of_nights']  # Calcola il totale del prezzo


columns_to_keep = ['booking_id', 'number_of_nights', 'date_check_in', 'date_check_out', 'total_price']  # Sostituisci con i nomi delle colonne che vuoi mantenere
merged_data = merged_data[columns_to_keep]
# Extract a list of random user_ids based on the number of rows in "booking.csv"
random_user_ids = np.random.choice(users_data['user_id'], size=len(merged_data))

# Add a new column "user_id" to the "booking.csv" DataFrame and assign the random user_ids
merged_data['user_id'] = random_user_ids
# Salva i risultati in un nuovo file CSV o utilizza il dataframe come necessario
merged_data.to_csv('booking.csv', index=False)


# Replace 'your_file.csv' with the actual path to your CSV file
file_path = 'booking.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

pd.set_option('display.max_columns', None)
# Display the first 5 rows of the DataFrame
print(df.head())
