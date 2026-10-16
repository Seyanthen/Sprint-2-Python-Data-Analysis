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
from matplotlib.ticker import FuncFormatter
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
        selected_area_name = "Boise Area"
        print("\nData will be loaded from Boise Area dataset.")
        break
    elif datArea == "2":
        selected_dataset_path = DATASET_2_PATH
        selected_area_name = "Idaho Falls Area"
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
# !!! Data that contains N/A values or invalid entries will be dropped 
# from the DataFrame to avoid errors in analysis. !!!

# Integer values are expected
integer_columns = ['PRICE', 'BEDS', 'LOT SIZE', 'YEAR BUILT', 'SQUARE FEET']

# BATHS and $/SQUARE FEET may contain decimal values.
decimal_columns = ['BATHS', '$/SQUARE FEET']

for column in integer_columns + decimal_columns: # convert to numeric type
    datSet[column] = pd.to_numeric(datSet[column], errors='coerce') 

datSet = datSet.dropna(subset=integer_columns).copy()  # Drop rows with NaN in integer columns

for column in integer_columns: # convert numeric format to integer type
    datSet[column] = datSet[column].astype(int) 


""" Step 5: Define and answer the first question about the selected dataset. """
# Question: Which homes under a selected price limit have the best price per quantity of BEDs?
# Apply a FILTER to datSet to keep only rows that meet the chosen conditions:
# Filter the dataframe by price under $500,000 and 2 bedrooms
filtered_beds_price = datSet.loc[(datSet["PRICE"] < 500000) & (datSet["BEDS"] >= 2)].copy()

# Print out the filtered and sorted results to the console
print("\nHomes in the selected area under $500,000 with at least 2 bedrooms:")
if filtered_beds_price.empty:
    print("No homes matched the selected conditions.")
else:
    # Apply a SORT to the filtered results by price per bedroom (low to high)
    filtered_beds_price["PRICE_PER_BEDROOM"] = ( 
        # Calculate price per bedroom
        filtered_beds_price["PRICE"] / filtered_beds_price["BEDS"]
    )
    filtered_beds_price = filtered_beds_price.sort_values(
        by="PRICE_PER_BEDROOM", 
        ascending=True
    )

    # Print summary statistics for the filtered results
    print(f"Number of matching homes: {len(filtered_beds_price)}")
    print(f"Average listing price: ${filtered_beds_price['PRICE'].mean():,.0f}")
    print(f"Average price per bedroom: ${filtered_beds_price['PRICE_PER_BEDROOM'].mean():,.0f}")

# Print top 10 columns of the filtered and sorted results to the console
print("\nTop 10 homes with the best price per bedroom:")
print(
    filtered_beds_price[
        ["ADDRESS", "CITY", "PRICE", "BEDS", "PRICE_PER_BEDROOM"]
    ].head(10).to_string(
        index=False,
        formatters={
            "PRICE": "${:,.0f}".format,
            "BEDS": "{:.0f}".format,
            "PRICE_PER_BEDROOM": "${:,.0f}".format
        }
    )
)


""" Step 6: Define and answer the second question about the selected dataset. """
# Question: What is the average listing price by city?
# Use an AGGREGATION such as groupby() with mean(), median(), or count().
# Display the grouped results and explain the pattern found.

# Group the cleaned listings by city and calculate the average listing price
# for each city.  Rows without a city or a valid price cannot contribute to
# this comparison, so they are excluded before the aggregation.
average_price_by_city = (
    datSet.dropna(subset=["CITY", "PRICE"])
    .groupby("CITY", as_index=False)["PRICE"]
    .mean()
    .rename(columns={"PRICE": "AVERAGE_LISTING_PRICE"})
    .sort_values("AVERAGE_LISTING_PRICE", ascending=False)
)

# Check for valid results after dropping invalid rows
print("\nAverage listing price by city:")
if average_price_by_city.empty:
    print("No city and price data was available for the aggregation.")
else:
    # Print the average listing price
    print(
        average_price_by_city.to_string(
            index=False,
            formatters={
                "AVERAGE_LISTING_PRICE": "${:,.0f}".format
            }
        )
    )

    # print the pattern found in the average listing price by city
    highest_city = average_price_by_city.iloc[0]
    lowest_city = average_price_by_city.iloc[-1]
    print(
        "Pattern found: {} has the highest average listing price at ${:,.0f},\n"
        "while {} has the lowest at ${:,.0f}.".format(
            highest_city["CITY"],
            highest_city["AVERAGE_LISTING_PRICE"],
            lowest_city["CITY"],
            lowest_city["AVERAGE_LISTING_PRICE"],
        )
    )



""" Step 7: Create a graph showing an important result. """
# The Step 6 aggregation is a useful result to visualize because a bar chart
# makes it easy to compare average listing prices across cities.
if average_price_by_city.empty:
    print("\nGraph was not created because no city and price data was available.")
else:
    # Create the output folder if it does not already exist.  This keeps the
    # program usable on a fresh checkout of the project.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    figure, axis = plt.subplots(figsize=(10, 6))
    bars = axis.bar(
        average_price_by_city["CITY"],
        average_price_by_city["AVERAGE_LISTING_PRICE"],
        color="steelblue",
    )

    # Format the vertical axis as currency so the chart matches the printed
    # aggregation and is easier to interpret at a glance.
    axis.yaxis.set_major_formatter(FuncFormatter(lambda value, position: f"${value:,.0f}"))
    axis.bar_label(
        bars,
        labels=[f"${value:,.0f}" for value in bars.datavalues],
        padding=3,
    )
    axis.set_title(f"Average Listing Price by City - {selected_area_name}")
    axis.set_xlabel("City")
    axis.set_ylabel("Average Listing Price")
    axis.tick_params(axis="x", rotation=30)

    # tight_layout prevents rotated city names and labels from being clipped.
    figure.tight_layout()
    figure.savefig(GRAPH_PATH, dpi=150)
    plt.close(figure)
    print(f"\nGraph saved to: {GRAPH_PATH}")