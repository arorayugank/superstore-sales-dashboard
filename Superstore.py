import pandas as pd
from sqlalchemy import create_engine

# Database connection info Replace with your actual MySQL credentials
username = "username"
password = "password"
host = "localhost"
port = 3306
database = "superstore_db"

# Create SQLAlchemy engine
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

# Read data from the 'Superstore' table
df = pd.read_sql("SELECT * FROM Superstore", engine)

# Data cleaning
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df = df.dropna(subset=['Order Date', 'Sales', 'Profit'])
df = df.drop_duplicates()
df['Profit_Margin'] = df['Profit'] / df['Sales']

# Write cleaned data back to MySQL
df.to_sql('Superstore', con=engine, if_exists='replace', index=False)

# Confirm success
print("\nData updated successfully!")
