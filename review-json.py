import pandas as pd
from jsonobject import JsonObject,write_to_json_file

# Read the CSV files
reviews_df = pd.read_csv('reviews.csv')
listings_df = pd.read_csv('listings.csv')

# Perform the join on listing_id from reviews.csv and id from listings.csv
merged_df = pd.merge(reviews_df, listings_df, left_on='listing_id', right_on='id')

# Select specific columns
selected_columns = ['id_x', 'score', 'comments', 'name', 'price']
result_df = merged_df[selected_columns]

#TODO move the fillna in the data-preparation in the file review-table
result_df = result_df.fillna('')
json_object_list = []

# Iterate through rows and save values in variables
for index, row in result_df.iterrows():
    review_id = row['id_x']
    score = row['score']
    comments = row['comments']
    if(review_id == 271117111):
        print(row['comments'])
    name = row['name']
    price = row['price']
    json_object = (
        JsonObject()
        .add_value("review_id", review_id)
        .add_value("score", score)
        .add_value("comments", comments)
        .add_value("listing_name", name)
        .add_value("price_for_night", price)
    )
    json_object_list.append(json_object.to_json_string())

write_to_json_file("review.json", json_object_list)

