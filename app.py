import pandas as pd
import sqlalchemy

def convert_dataframe_to_sql(dataframe, table_name, connection):
    dataframe.to_sql(table_name, connection, index=False, if_exists='append')

# Read csv files into pandas
sales_filepath = "Resources/vg_sales.csv"
reviews_filepath = "Resources/vg_reviews.csv"
df_sales = pd.read_csv(sales_filepath, encoding='utf-8')
df_reviews = pd.read_csv(reviews_filepath, encoding='utf-8')

# Filter, select columns, and rename column for N64 sales DataFrame
n64_sales = df_sales.loc[df_sales["Platform"] == "N64", ['Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales']].reset_index(drop=True)

# Filter, select columns, and rename column for N64 reviews DataFrame
n64_reviews = df_reviews.loc[df_reviews["platform"] == "Nintendo 64", ['title', 'score', 'score_phrase', 'editors_choice']].rename(columns={"title": "Name"}).reset_index(drop=True)

# Establish parameters for SQL connection to Amazon RDS server
database_username = 'group04'
database_password = 'XXXXX'
database_host = 'XXXXX.rds.amazonaws.com'
database_name = 'group04'
database_connection_url = f'mysql+mysqlconnector://{database_username}:{database_password}@{database_host}/{database_name}'

# Create database connection
database_connection = sqlalchemy.create_engine(database_connection_url)

# Convert DataFrames to SQL tables and upload to the database
convert_dataframe_to_sql(n64_reviews, 'N64_reviews', database_connection)
convert_dataframe_to_sql(n64_sales, 'N64_sales', database_connection)
