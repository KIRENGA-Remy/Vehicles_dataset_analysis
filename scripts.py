import pandas as pd


file_path = 'vehicles.csv'


try:
    data = pd.read_csv(file_path)

    print("Dataset successfully loaded!")
    print(data.head())

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except pd.errors.EmptyDataError:
    print("Error: The file is empty.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    