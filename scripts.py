import pandas as pd
import matplotlib.pyplot as plt

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

    #count : return total numbers of values without null values
    print("Studying count")
    print(data.count())

    #value_counts: counts unique categories, like audi=7, bmw=2, 
    print("Studying value_counts")
    print(data.value_counts())

    #nunique: counts number of unique values
    print("Studying nunique")
    print(data.nunique())

    #describe: describes counts, mean, frequency, std:standard deviation,
    print("Studying describe")
    print(data.describe())
    # but on quantitative data it dont describe these, it gives count, unique,top and frequency only
    # print("Describe on quantitative data")
    # sdf = data[['manufacturer','color','body_type','engine_type']]
    # print(sdf.describe())

    # print(sdf['manufacturer'[:10]]) # equivalence: sdf['manufacturer'].head(10)

    # print(sdf['manufacturer'][3:10]) #selecting from 3 to ten(10)

    #astype: when cleaning is done before

    data['proposed_purchase_price'].plot.hist(bins=30, alpha=0.7,color='blue')
    plt.savefig('./purchase_price.png', format='png', dpi=400)
    plt.show()

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except pd.errors.EmptyDataError:
    print("Error: The file is empty.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

