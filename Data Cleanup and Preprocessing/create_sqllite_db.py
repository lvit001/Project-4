# import dependencies
import pandas as pd
import sqlite3

# connect to db
conn = sqlite3.connect('../Data/diseases.sqlite')

# read the csv data into a dataframe
df = pd.read_csv('../Data/encoded_data.csv')

# send it to the database (replace 'passenger' with your table name and 'id' with your primary key column)
df.to_sql('diseases', conn, index=False, if_exists='replace')
conn.close()