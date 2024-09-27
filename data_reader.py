import csv
import os
import pandas as pd

def read_file(csv_file, column_name):
    # Read the CSV file using pandas
    df = pd.read_excel(csv_file) # 'on_bad_lines=skip' to skip invalid lines

    # Check if the column exists in the dataframe
    if column_name in df.columns:
        return df[column_name].tolist()  # Return the column as a list
    else:
        print(f"Column '{column_name}' not found in the CSV file.")
        return []