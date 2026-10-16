# Roofer (1.0)

Housing Market Analysis: Analyze housing market data to identify housing trends in Idaho by select cities, and identify best price per room listings

Project Requirements:

1. Find or create a dataset that interests you.
2. Use software to analyze and answer two questions about the data.
3. Software analysis should include a filter.
4. Software analysis should include a sort.
5. Software analysis should include an aggregation.

Stretch Challenge: Update your software so it draws a graph showing some of the results.

## Instructions for Build and Use

Steps to build and/or run the software:

1. Install Python 3.11.4 or another compatible Python 3 version.
2. Install the required third-party libraries with `python -m pip install pandas matplotlib`.
3. Confirm that `data/ID-1.csv` and `data/ID-2.csv` are present in the project folder.
4. From the project directory, run the program with `python main.py`.

Instructions for using the software:

1. When prompted, enter `1` to analyze the Boise Area dataset or `2` to analyze the Idaho Falls Area dataset.
2. The program loads only the selected dataset, removes the MLS notice row, removes unused columns, and converts the analysis fields to numeric values.
3. The first analysis filters listings under $500,000 with at least two bedrooms, sorts the matching listings by price per bedroom, and reports summary information.
4. The second analysis groups listings by city and reports the average listing price for each city, from highest to lowest.
5. The program creates a bar chart of average listing price by city and saves it to `output/housing_market_results.png`.
6. Review the printed results and generated chart for the selected area.

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Python 3.11.4
* pandas 2.0.3
* matplotlib 3.8.1
* `pathlib`, included with the Python standard library

Project data and output folders:

* `data/` contains the input CSV datasets.
* `output/` is reserved for generated charts and other analysis results.

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Pandas 10 Minute Tutorial](https://pandas.pydata.org/docs/user_guide/10min.html#min)
* [Pandas Getting Started Tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
* [Pandas Example with Titanic Data](https://www.kaggle.com/code/faressayah/data-science-best-practices-using-pandas-titanic)
* [Exploratory Data Analysis with Pandas](https://www.kaggle.com/kashnitsky/topic-1-exploratory-data-analysis-with-pandas)
* [YouTube Learn Python for Beginners](https://www.youtube.com/watch?v=fWjsdhR3z3c)
* [W3 Schools Python Tutorial](https://www.w3schools.com/python/default.asp)


## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Dynamic Filter and Sort Selections
* [ ] Add error handiling for CSV files
