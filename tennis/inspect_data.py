import pandas as pd
import re

def inspect_data(data):
    return data

# Load the data from the CSV file
def load_data(filename):
    return pd.read_csv(filename)

def main():
    filename = 'tennis/results.csv'
    data = load_data(filename)
    
    # Set pandas display options to show more rows
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    
    # Inspect the data to understand the seed representation
    print(f"\n{'='*20} Inspecting the data {'='*20}")
    print(inspect_data(data))
    print("\n\n")

    # Other function calls here...

if __name__ == "__main__":
    main()