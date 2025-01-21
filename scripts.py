#TO RUN: jupyter notebook
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

file_path = 'vehicles.csv'


try:
    data = pd.read_csv(file_path)
    print("Load last 5 rows using tail")
    print(data.tail())

    print("Load fist 5 rows using head")
    print(data.head())

    print("Load first 5 and last 5 rows using info")
    print(data.info) # combines head and tail functionality, transposed
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

    #describe:summarize the numerical (quantitative) columns.
    #by providing numeric summary statistics like counts, mean, frequency, std:standard deviation,...
    print("Studying describe")
    print(data.describe())
    #but on categorical data it don't describe these, it gives count, unique,top and frequency only
    #which are non-numeric summary statistics
    print("Describe on quantitative data")
    sdf = data[['manufacturer','color','body_type','engine_type']]
    print(sdf.describe())

    print(sdf['manufacturer'][:10]) # slicing column manufacturer, equivalence: sdf['manufacturer'].head(10)

    print(sdf['manufacturer'][3:10]) #selecting from 3 to ten(10)

    #astype: when cleaning is done before

    # data['proposed_purchase_price'].plot.hist(bins=30, alpha=0.7,color='blue')
    # plt.savefig('./purchase_price.png', format='png', dpi=400)
    # plt.show()


#     What Are Bins?
# Bins are the intervals (or "buckets") into which the data values are sorted.
# Each bin represents a range of data, and the height of the bar for that bin corresponds to the number of data points that fall within that range.

# Bin Width= Range of Data / Number of Bins

#BAR CHART
    bar_chart = data['manufacturer']
    unique_values, counts = np.unique(bar_chart, return_counts=True)
    plt.figure(figsize=(23,3))
    plt.bar(unique_values, counts, alpha=0.2, color='blue', edgecolor='white')
    plt.savefig('pic.png', format='png', dpi=300)
    plt.show()

    #USE OF XTICKS ON HISTOGRAM
    number_of_bins=int(np.ceil(np.log2(len(bar_chart))+1)) #sturgey's rule: how to calculate the number of bins
    plt.figure(figsize=(23,3))
    plt.hist(bar_chart, bins=number_of_bins, edgecolor='yellow')
    plt.xticks(unique_values)
    plt.show()

    for col in ['manufacturer','year','color', 'body_type', 'engine_type', 'transmission', 'fuel_type', 'seating_capacity', 'vehicle_condition_status', 'owner_profession', 'owner_age']:
        #vehicles_in_district_counts = inner_merged_df[col].value_counts()
        plt.figure(figsize=(23, 5))
        ax = sns.countplot(x=col, data=data, palette='colorblind', order=data[col].value_counts().index)
        plt.grid(color="green", linestyle="--", linewidth=0.5)
        plt.title(f"{col.capitalize()} with their counts", fontdict={"family": "serif", "color": "blue", "size": 20})
        plt.xticks(rotation=90) # Rotate x labels for better visibility
        # Add counts at the top of each bar
        for p in ax.patches:
            ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', fontsize=12, color='green', rotation=90)
        plt.show()

    #A LINE CHART
    for col in [
        'manufacturer',
        'year',
        'color',
        'body_type',
        'engine_type',
        'transmission',
        'fuel_type',
        'seating_capacity',
        'vehicle_condition_status',
        'owner_profession',
        'owner_age']:
        plt.figure(figsize=(23, 5))
        # Count values for the current column
        counts = data[col].value_counts().sort_index()
        # Create a line chart
        plt.plot(counts.index, counts.values, marker='o', linestyle='-', color='blue')
        # Customize the plot
        plt.grid(color="green", linestyle="--", linewidth=0.5)
        plt.title(f"{col.capitalize()} Counts", fontdict={"family": "serif", "color": "blue", "size": 20})
        plt.xlabel(col.capitalize(), fontsize=14)
        plt.ylabel('Counts', fontsize=14)
        plt.xticks(rotation=90)  # Rotate x labels for better visibility
        # Annotate counts on the line chart
        for x, y in zip(counts.index, counts.values):
            plt.text(x, y, str(y), ha='center', va='bottom', fontsize=12, color='green')
        plt.tight_layout()  # Adjust layout
        plt.show()

        #scatter plot
        x=data['selling_price'][:100]
        y=data['proposed_purchase_price'][:100]
        plt.scatter(x,y, color='red', alpha=0.5, edgecolors='b', linewidths=2)
        plt.show()


except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except pd.errors.EmptyDataError:
    print("Error: The file is empty.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

