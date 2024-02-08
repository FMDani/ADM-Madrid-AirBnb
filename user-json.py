import pandas as pd
from jsonobject import JsonObject,write_to_json_file
import sys
import random

# Read the CSV files
reviews_df = pd.read_csv('reviews.csv')
listings_df = pd.read_csv('listings.csv')
users_df = pd.read_csv('users.csv')
bookings_df = pd.read_csv('booking.csv')

pd.set_option('display.max_columns', None)

#TODO move the fillna in the data-preparation in the file review-table
#result_df = result_df.fillna('')
json_object_list = []

# Iterate through rows and save values in variables
for index, row in users_df.iterrows():
    user_id = row['user_id']
    name = row['name']
    surname = row['surname']
    json_object_list_r = []
    for index_r, row_r in reviews_df.iterrows():
        if(user_id == row_r['reviewer_id']):            
            review_id = row_r['id']
            json_object_reviewid_score = (
                JsonObject()
                .add_value("review_id", review_id)
            )
            json_object_review = (
                JsonObject()
                .add_value("review", json_object_reviewid_score)
            )
            json_object_list_r.append(json_object_review)
    json_object_list_b = []
    for index_b, row_b in bookings_df.iterrows():
        if(user_id == row_b['user_id']):            
            booking_id = row_b['booking_id']
            json_object_bookingid_score = (
                JsonObject()
                .add_value("booking_id", booking_id)
            )
            json_object_booking = (
                JsonObject()
                .add_value("booking", json_object_bookingid_score)
            )
            json_object_list_b.append(json_object_booking)
    json_object_list_l = []
    for index_l, row_l in listings_df.iterrows():
        if(user_id == row_l['host_id']):            
            listing_id = row_l['id']
            json_object_listingid_score = (
                JsonObject()
                .add_value("listing_id", listing_id)
            )
            json_object_listing = (
                JsonObject()
                .add_value("listing", json_object_listingid_score)
            )
            json_object_list_l.append(json_object_listing)
    
    json_object = (
        JsonObject()
        .add_value("user_id", user_id)
        .add_value("name", name)
        .add_value("surname", surname)

        .add_value("Review_a", json_object_list_r)
        .add_value("Do_a", json_object_list_b)
        .add_value("Host", json_object_list_l)

    )
    json_object_list.append(json_object.to_json_string())

write_to_json_file("user.json", json_object_list)