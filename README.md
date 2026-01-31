# Food Delivery Data Analysis Project

## Project Overview
This project demonstrates how to integrate and analyze real-world datasets stored in 
different formats (CSV, JSON, and SQL). The goal is to create a unified dataset and 
derive insights related to user behavior, restaurant performance, and revenue trends.

## Datasets Used
- orders.csv – Transactional order data
- users.json – User master data
- restaurants.sql – Restaurant master data

## Technologies Used
- Python
- Pandas
- SQLite
- Jupyter Notebook / Python Script

## Approach
1. Loaded transactional data from CSV using Pandas.
2. Loaded user data from JSON using Pandas.
3. Loaded restaurant data from SQL using SQLite.
4. Merged datasets using LEFT JOIN to retain all order records.
5. Created a final dataset for analysis and reporting.

## Key Analysis Areas
- Order trends over time
- City-wise and cuisine-wise revenue
- Gold vs Regular membership impact
- Average order value analysis
- Restaurant rating and revenue relationship

## Output
- final_food_delivery_dataset.csv – Combined dataset used for analysis

## Author
Apurva Joshi
