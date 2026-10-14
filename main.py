"""
Housing market data analysis project.

This Project was built with Python 3.11.4, pandas 2.0.3, and matplotlib 3.8.1.

Agentic AI assistance was used in this project:
 1. The AI provided a step-by-step outline of the project requirements and analysis steps.
 2. The AI provided guidance on how to implement the analysis steps in Python.
 3. The AI built the graphing code to visualize the analysis results. 
"""

""" Step 1: Import the libraries needed for the analysis. """
# pandas will load, clean, filter, sort, and aggregate the CSV data.
# matplotlib will create a graph from the analysis results.
# pathlib will create file paths that work across operating systems.
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


""" Step 2: Configure the project folders and input/output file paths. """
# The CSV files are kept in data/, and future charts will be saved in output/.
PROJECT_DIR = Path(__file__).parent
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = PROJECT_DIR / "output"

DATASET_1_PATH = DATA_DIR / "ID-1.csv"
DATASET_2_PATH = DATA_DIR / "ID-2.csv"
GRAPH_PATH = OUTPUT_DIR / "housing_market_results.png"

# Report Program Status
print("Program imported libraries and configured file paths successfully.")

""" Step 3: Select and load one dataset when the program starts. """
# Display a numbered menu containing the available dataset choices.
# Ask the user to choose a dataset before reading any CSV file.
# Validate the response so only a valid menu option is accepted.
# Convert the selection into one input path: DATASET_1_PATH or DATASET_2_PATH.
while True:
    print('Please select a dataset to analyze:')
    print('1. Boise Area')
    print('2. Idaho Falls Area')
    datArea = input("Enter 1 or 2: ").strip()

    if datArea == "1":
        selected_dataset_path = DATASET_1_PATH
        print("\nData will be loaded from Boise Area dataset.")
        break
    elif datArea == "2":
        selected_dataset_path = DATASET_2_PATH
        print("\nData will be loaded from Idaho Falls Area dataset.")
        break
    else:
        print("\nInvalid selection. Please choose 1 or 2.")

# Use pandas to read only the selected CSV into one DataFrame.
datSet = pd.read_csv(selected_dataset_path)

""" Step 4: Clean and prepare the selected DataFrame. """
# Remove any non-data notice rows that appear in the CSV files.
# Drop the first MLS notice row
datSet = datSet.iloc[1:].reset_index(drop=True)

# Drop unnecessary columns that are not needed for the analysis.
columns_to_remove = [
    'SALE TYPE', 'SOLD DATE', 'LOCATION', 'DAYS ON MARKET', 'HOA/MONTH',
    'STATUS', 'NEXT OPEN HOUSE START TIME', 'NEXT OPEN HOUSE END TIME',
    'URL (SEE https://www.redfin.com/buy-a-home/comparative-market-analysis FOR INFO ON PRICING)',
    'SOURCE', 'MLS#', 'FAVORITE', 'INTERESTED', 'LATITUDE', 'LONGITUDE'
]
datSet = datSet.drop(columns=columns_to_remove, errors='ignore')

# Convert numeric columns such as PRICE, BEDS, BATHS, SQUARE FEET,
# LOT SIZE, YEAR BUILT, and $/SQUARE FEET to appropriate numeric data types.
# Assign the converted values back to datSet; conversion alone does not change
# the original DataFrame. BATHS and $/SQUARE FEET may contain decimal values.
numeric_columns = [
    'PRICE', 'BEDS', 'BATHS', 'LOT SIZE', 'YEAR BUILT',
    'SQUARE FEET', '$/SQUARE FEET'
]
for column in numeric_columns:
    datSet[column] = pd.to_numeric(datSet[column], errors='coerce')

print(datSet.head())

# Decide how missing values should be handled and document that decision.
# Invalid or missing numeric values are currently represented as NaN.
# Before analysis, decide whether to leave, remove, or replace those values.
# Keep these steps written against the selected DataFrame so the same analysis
# works regardless of which dataset the user chooses.




""" Step 5: Continue working with the selected dataset. """
# The dataset chosen in Step 3 is now stored in datSet and has been cleaned.
# Use datSet for all remaining analysis so the same steps work for either
# the Boise Area or Idaho Falls Area dataset.
# Do not combine the datasets because this program analyzes one selection
# during each run.


""" Step 6: Define and answer the first question about the selected dataset. """
# Example question: Which homes under a selected price limit have the largest
# square footage in the selected area?
# Apply a FILTER to datSet to keep only rows that meet the chosen conditions.
# Apply a SORT to the filtered results by square footage or price.
# Display the most relevant rows and explain what the results show.


""" Step 7: Define and answer the second question about the selected dataset. """
# Example question: What is the average listing price by city or property type
# within the selected area?
# Use an AGGREGATION such as groupby() with mean(), median(), or count().
# Display the grouped results and explain the pattern found.


""" Step 8: Create a graph showing an important result. """
# Select a useful result from the analysis of the selected dataset.
# Choose an appropriate chart type, such as a bar chart of average price by
# city or a scatter plot comparing square footage and price in that area.
# Add a clear title, axis labels, and legend if needed.
# Save the finished graph to GRAPH_PATH and/or display it on screen.


""" Step 9: Review the program output. """
# Confirm that the selected dataset loaded correctly and that the cleaning
# steps removed the MLS notice row and unnecessary columns.
# Confirm that both questions are answered and that the filter, sort, and
# aggregation are visible in the analysis.
# Confirm that the graph represents only the selected area and is readable.
# Add brief comments or printed labels so another person can follow the results.
