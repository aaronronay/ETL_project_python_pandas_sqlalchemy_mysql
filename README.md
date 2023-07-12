# README

This code reads CSV files, performs data filtering and selection using pandas, establishes a SQL connection, and converts DataFrames to SQL tables for uploading to a database. Error handling is implemented to handle potential exceptions during the process.

## Dependencies

- pandas
- sqlalchemy

## Setup

1. Ensure that the necessary dependencies are installed. You can install them using pip:

pip install pandas sqlalchemy

2. Place the CSV files (`vg_sales.csv` and `vg_reviews.csv`) in a folder named "Resources" in the same directory as the code file.

3. Update the following parameters in the code:

- `sales_filepath`: Path to the `vg_sales.csv` file.
- `reviews_filepath`: Path to the `vg_reviews.csv` file.
- `database_username`: Your database username.
- `database_password`: Your database password.
- `database_host`: Your database host.
- `database_name`: Your database name.

## Execution

1. Run the code using a Python interpreter.

python your_code_file.py


2. The program will read the CSV files, filter and select the required columns, establish a SQL connection, and convert the DataFrames to SQL tables.

3. Progress and error messages will be displayed in the console.

## Notes

- Ensure that the necessary MySQL Connector/Python driver is installed.
- Make sure the database connection parameters are accurate and correspond to your specific database setup.

Feel free to customize the code and parameters based on your requirements.
