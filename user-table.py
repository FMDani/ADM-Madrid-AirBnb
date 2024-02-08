import pandas as pd
from faker import Faker
import math

# Inizializza il generatore di dati casuali
fake = Faker()

# Carica la tabella reviews_details.csv
reviews_detail = pd.read_csv('reviews.csv')
listings_detail = pd.read_csv('listings.csv')

# Estrai le colonne "reviewer_id" e "reviewer_name"
users_data = pd.merge(reviews_detail, listings_detail, how='outer', left_on='reviewer_id', right_on='host_id')

df = pd.DataFrame(columns=['colonna1', 'colonna2'])
array = []

for index, row in users_data.iterrows():
    if not(math.isnan(row['reviewer_id'])):
        array.append(int(row['reviewer_id']))
    else:
        array.append(int(row['host_id']))

users_data['user_id'] = array

# Convert 'user_id' column to a DataFrame
users_data = users_data[['user_id']]

# Elimina i duplicati basati su "user_id"
users_data = users_data.drop_duplicates('user_id')

# Genera nomi e cognomi casuali utilizzando faker
users_data['name'] = [fake.first_name() for _ in range(len(users_data))]
users_data['surname'] = [fake.last_name() for _ in range(len(users_data))]

# Salva la nuova tabella Users.csv
users_data.to_csv('users.csv', index=False)

# Visualizza le prime 5 righe della nuova tabella
print(users_data.head())

