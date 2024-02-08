import pandas as pd
from jsonobject import JsonObject,write_to_json_file
import sys
import random

# Read the CSV files
reviews_df = pd.read_csv('reviews.csv')
listings_df = pd.read_csv('listings.csv')

users_df = pd.read_csv('users.csv')

pd.set_option('display.max_columns', None)

#TODO move the fillna in the data-preparation in the file review-table
listings_df = listings_df.fillna('')
json_object_list = []

# Iterate through rows and save values in variables
for index, row in listings_df.iterrows():
    listing_id = row['id']
    listing_name = row['name']
    description = row['description']
    host_id = row['host_id']
    json_object_list_r = []
    for index_r, row_r in reviews_df.iterrows():
        if(listing_id == row_r['listing_id']):            
            review_id = row_r['id']
            score = row_r['score']
            json_object_reviewid_score = (
                JsonObject()
                .add_value("review_id", review_id)
                .add_value("score", score)
            )
            json_object_review = (
                JsonObject()
                .add_value("review", json_object_reviewid_score)
            )
            json_object_list_r.append(json_object_review)
    name = None
    surname = None

    for index_u, row_u in users_df.iterrows():
        if(host_id == row_u['user_id']):            
            name = row_u['name']
            surname = row_u['surname']
            break         

    room_type = row['room_type']
    host_score = random.randint(1, 5)
    
    json_object = (
        JsonObject()
        .add_value("listing_id", listing_id)
        .add_value("listing_name", listing_name)
        .add_value("description", description)
        .add_value("Has", json_object_list_r)
        .add_value("room_type", room_type)
        .add_value("name", name)
        .add_value("surname", surname)
        .add_value("host_score", host_score)
    )

    json_object_list.append(json_object.to_json_string())

write_to_json_file("listing.json", json_object_list)

