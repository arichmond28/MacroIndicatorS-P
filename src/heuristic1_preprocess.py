import csv
import pandas as pd
from datetime import datetime

def data_load():
    with open('/Users/andrewrichmond/Desktop/MacroIndicatorS-P/data/DATA.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    with open('/Users/andrewrichmond/Desktop/MacroIndicatorS-P/data/SPX.csv', 'r') as f:
        reader = csv.reader(f)
        labels = list(reader)
    return data, labels

def preprocess(data):
    # Transpose the data to iterate over columns
    transposed_data = list(zip(*data))
    
    columns_to_remove = set()
    for col_index, col in enumerate(transposed_data):
        if '' in col:
            columns_to_remove.add(col_index)
    
    filtered_data = [
        [value for col_index, value in enumerate(row) if col_index not in columns_to_remove]
        for row in data
    ]
    
    filtered_data = [row[1:] for row in filtered_data]
    
    return filtered_data[1:]

def percentChange(data):
    percent_changes = []
    
    for i in range(1, len(data)):
        row_changes = []
        for j in range(len(data[i])):
            previous_value = float(data[i-1][j])
            current_value = float(data[i][j])
            change = ((previous_value - current_value) / previous_value) * 100
            row_changes.append(change)
        percent_changes.append(row_changes)
    
    return percent_changes


def compare_monthly_open(data, start_date="2002-05-01", end_date="2022-05-01"):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    monthly_open_comparison = []
    previous_open = None
    
    for row in data[1:]:
        date = datetime.strptime(row[0], "%Y-%m-%d")
        if date.day == 1 and start_date <= date <= end_date:
            current_open = float(row[1])
            if previous_open is not None:
                if current_open > previous_open:
                    monthly_open_comparison.append(1)
                else:
                    monthly_open_comparison.append(0)
            previous_open = current_open
    
    return monthly_open_comparison[::-1]
    




if __name__ == '__main__':
    data = data_load()[0]
    data = preprocess(data)
    data = percentChange(data)
    
    labels = data_load()[1]
    labels = compare_monthly_open(labels)
    
    output_file = "/Users/andrewrichmond/Desktop/MacroIndicatorS-P/data/processed_labels.csv"

    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        for item in labels:
            writer.writerow([item])
