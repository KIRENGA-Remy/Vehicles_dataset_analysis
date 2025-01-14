import pandas as pd


file_path = 'vehicles.csv'


try:
    data = pd.read_csv(file_path)
    print("Load last 5 rows using tail")
    print(data.tail())

    print("Load fist 5 rows using head")
    print(data.head())

    print("Load first 5 and last 5 rows using info")
    print(data.info) # combines head and tail functionality
    print(data.info()) #it is an error, not transposed, it is like a table

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except pd.errors.EmptyDataError:
    print("Error: The file is empty.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    