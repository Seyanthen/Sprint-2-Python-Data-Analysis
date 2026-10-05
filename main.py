import pandas as pd

print("Hello, World!")

name = input("What is your name? ")
print(f"Hello, {name}! Welcome to the program.")

# Create a quick DataFrame
data = {'Product': ['Apparel', 'Electronics'], 'Status': ['In Stock', 'Pre-order']}
df = pd.DataFrame(data)

print("Pandas version:", pd.__version__)
print(df)