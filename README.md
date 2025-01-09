# Vehicles Data Analysis Project

This project provides an analysis of a dataset of vehicles to uncover insights into car sales trends. It demonstrates data cleaning, manipulation, exploratory analysis, and visualization techniques using Python. The project is structured for easy reproducibility and visualization with tools like Power BI or Tableau.

---

## 📂 Folder Structure
vehicles-data-analysis/ │ ├── .ipynb_checkpoints/ # Jupyter Notebook checkpoints ├── venv/ # Virtual environment (dependencies) ├── vehicles.csv # Original dataset ├── data_cleaning.ipynb # Jupyter Notebook for cleaning data ├── README.md # Project documentation ├── requirements.txt # Python dependencies ├── scripts.py # Python script for initial data handling ├── sorting_sp.ipynb # Jupyter Notebook for sorting operations ├── vehicles_cleaned.csv # Cleaned dataset (to be generated)

yaml
Copy code

---

## 📜 Project Overview

The goal of this project is to analyze vehicle sales data to identify key patterns and insights. The dataset includes details like manufacturer, year, selling price, and vehicle condition, among others.

---

## 🛠️ Environment Setup

Follow these steps to set up your environment and reproduce the analysis:

### 1. Clone the Repository
```bash
git clone https://github.com/username/vehicles-data-analysis.git
cd vehicles-data-analysis
2. Set Up the Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Launch Jupyter Notebook
bash
Copy code
jupyter notebook
Open and run the notebooks (data_cleaning.ipynb or sorting_sp.ipynb) to explore and analyze the data.

📂 Dataset Description
The dataset (vehicles.csv) contains the following columns:

Column Name	Description
vin	Vehicle Identification Number (Unique Identifier)
manufacturer	Name of the manufacturer
year	Manufacturing year of the vehicle
color	Color of the vehicle
body_type	Type of the vehicle body (e.g., SUV, Sedan)
engine_type	Type of engine (e.g., Diesel, Petrol)
transmission	Type of transmission (e.g., Manual, Automatic)
fuel_type	Type of fuel (e.g., Diesel, Petrol)
seating_capacity	Number of seats in the vehicle
kilometers_driven	Total kilometers the vehicle has been driven
vehicle_condition_status	Condition of the vehicle (e.g., New, Used)
selling_price	Price at which the vehicle is being sold
owner_name	Name of the vehicle owner
owner_profession	Profession of the vehicle owner
owner_age	Age of the owner
owner_district	District where the owner resides
proposed_purchase_price	Proposed price for purchasing the vehicle
purchase_date	Date of vehicle purchase
🛠️ Code Highlights
Data Cleaning
The script in data_cleaning.ipynb cleans and prepares the dataset:

Converts selling_price to numeric by removing commas and handling non-numeric values.
Handles missing values and identifies data types for further processing.
python
Copy code
import pandas as pd

file_path = 'vehicles.csv'

try:
    data = pd.read_csv(file_path)
    print("Dataset successfully loaded!")
    print(data.dtypes)

    # Clean selling_price
    data['selling_price'] = data['selling_price'].astype(str).str.replace(',', '', regex=True)
    data['selling_price'] = pd.to_numeric(data['selling_price'], errors='coerce')
    print(data['selling_price'].head())
except Exception as e:
    print(f"An error occurred: {e}")
Exploratory Data Analysis
The following insights are explored:

Distribution of selling_price
Relationship between year and selling_price
Selling price trends by vehicle condition
📊 Visualizations
Key insights are visualized using Python (Matplotlib and Seaborn) and external tools like Power BI or Tableau. Examples:

Distribution of Selling Prices
Year vs. Selling Price
Selling Price by Vehicle Condition
🚀 Export for External Tools
After processing the dataset, save the cleaned data for further visualization in Power BI or Tableau:

python
Copy code
data.to_csv('vehicles_cleaned.csv', index=False)
🔍 Next Steps
Integrate advanced visualizations in Tableau/Power BI dashboards.
Add predictive models for estimating vehicle prices.
🤝 Contributing
Contributions are welcome! Feel free to submit pull requests or report issues.

📝 License
This project is open-source under the MIT License.