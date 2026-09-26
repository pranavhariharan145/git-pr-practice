# # Here we will use customers csv file to convert to json and log function calls with decorator

import csv
import json
# Our Decorator function to Log name of the function, argumens passed
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Logs:")
        print("Function Called: ", func.__name__)
        print("Positional arguments passed: ", args)
        print("Keyword arguments passed: ", kwargs)
        return func(*args, **kwargs)
    return wrapper

@decorator
def csv_to_json(csv_file_path: str, json_file_path:str):
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        # using dictreader to read the csv file and to convert each rows as dictionaries
        csv_reader = csv.DictReader(csv_file)          
        data = list(csv_reader)

    # json dumps to convert the lists containing csv to dictionaries with indent = 4 for pretty printing
    json_data = json.dumps(data, indent=2)

    # save the json to file 
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json_file.write(json_data)

    return json_data

# Usage: should have customers-100.csv to read and customers.json to write
if __name__ == "__main__":
    # 1. csv file to demonstrate
    sample_csv = "customers-100.csv"
    # 2. run the decorated transformation function
    output_json = "customers.json"
    result = csv_to_json(sample_csv,output_json)

