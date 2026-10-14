"""
Housing market data analysis project.

This Project was built with Python 3.11.4, pandas 2.0.3, and matplotlib 3.8.1.

Agentic AI assistance was used in this project:
 1. The AI provided a step-by-step outline of the project requirements and analysis steps.
 2. The AI provided guidance on how to implement the analysis steps in Python.
 3. The AI built the graphing code to visualize the analysis results. 
"""

# Step 1: Import the libraries needed for the analysis.
# pandas will load, clean, filter, sort, and aggregate the CSV data.
# matplotlib will create a graph from the analysis results.
# pathlib will create file paths that work across operating systems.
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# Step 2: Configure the project folders and input/output file paths.
# The CSV files are kept in data/, and future charts will be saved in output/.
PROJECT_DIR = Path(__file__).parent
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = PROJECT_DIR / "output"

DATASET_1_PATH = DATA_DIR / "ID-1.csv"
DATASET_2_PATH = DATA_DIR / "ID-2.csv"
GRAPH_PATH = OUTPUT_DIR / "housing_market_results.png"

print("Program imported libraries and configured file paths successfully.")
# Step 3: Load the datasets into pandas DataFrames.
# Read both CSV files and store them in clearly named variables.
# Check the first few rows, column names, data types, and missing values.
Boise = pd.read_csv('data\\ID-1.csv')
#print(Boise) 

IDFalls = pd.read_csv('data\\ID-2.csv')
#print(IDFalls) 
print(IDFalls.head(3))

# Step 4: Clean and prepare the data.
# Remove any non-data notice rows that appear in the CSV files.
# Convert numeric columns such as PRICE, BEDS, BATHS, SQUARE FEET,
# DAYS ON MARKET, and $/SQUARE FEET to appropriate numeric data types.
# Decide how missing values should be handled and document that decision.

# Drop the First row
IDFalls = IDFalls.drop([0], axis=0)
# Drop unnecessary columns that are not needed for the analysis.
IDFalls.drop(['SALE TYPE', 'SOLD DATE', 'LOCATION', 'DAYS ON MARKET', 'HOA/MONTH', 'STATUS', 'NEXT OPEN HOUSE START TIME', 'NEXT OPEN HOUSE END TIME', 'URL (SEE https://www.redfin.com/buy-a-home/comparative-market-analysis FOR INFO ON PRICING)', 'SOURCE', 'MLS#', 'FAVORITE', 'INTERESTED', 'LATITUDE', 'LONGITUDE'], axis=1, inplace=True)
print(IDFalls.head())


# Step 5: Combine the datasets if comparing both housing market areas.
# Add a source or area label to each DataFrame before combining them.
# Concatenate the DataFrames into one DataFrame for consistent analysis.


# Step 6: Define and answer the first question about the housing data.
# Example question: Which active homes under a selected price limit have the
# largest square footage?
# Apply a FILTER to keep only rows that meet the selected conditions.
# Apply a SORT to order the filtered results by square footage or price.
# Display the most relevant rows and explain what the results show.


# Step 7: Define and answer the second question about the housing data.
# Example question: What is the average listing price by city or property type?
# Use an AGGREGATION such as groupby() with mean(), median(), count(),
# or another appropriate summary calculation.
# Display the grouped results and explain the pattern found.


# Step 8: Create a graph showing an important result.
# Select a useful result DataFrame from the analysis above.
# Choose an appropriate chart type, such as a bar chart of average price by
# city or a scatter plot comparing square footage and price.
# Add a clear title, axis labels, and legend if needed.
# Save the finished graph to GRAPH_PATH and/or display it on screen.


# Step 9: Review the program output.
# Confirm that the two questions are answered, that the filter, sort, and
# aggregation are visible in the analysis, and that the graph is readable.
# Add brief comments or printed labels so another person can follow the results.
