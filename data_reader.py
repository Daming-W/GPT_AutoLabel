import csv
import os
import pandas as pd

def read_file(csv_file, column_name):
    # Read the CSV file using pandas
    df = pd.read_csv(csv_file, encoding='GBK')

    # Check if the column exists in the dataframe
    return df[column_name].tolist()  # Return the column as a list


def write_txt(file_path, data_list):
    # Open the file in write mode
    with open(file_path, mode='w', encoding='utf-8') as file:
        # Iterate over the list and write each item to the file
        for item in data_list:
            print(item)
            file.write(f"{item}\n") 