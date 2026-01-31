import pandas as pd
import sqlite3

# Load CSV data
orders = pd.read_csv("data/orders.csv")

# Load JSON data
users = pd.read_json("data/users.json")

# Load SQL data
conn = sqlite3.connect(":memory:")
with open("data/restaurants.sql", "r") as f:
    conn.executescript(f.read())

restaurants = pd.read_sql("SELECT * FROM restaurants", conn)

# Merge datasets using LEFT JOIN
final_df = orders.merge(users, on="user_id", how="left") \
                 .merge(restaurants, on="restaurant_id", how="left")

# Save final dataset
final_df.to_csv("final_food_delivery_dataset.csv", index=False)

print("Final dataset created successfully.")