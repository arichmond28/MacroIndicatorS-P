import csv

def data_load():
    with open('/Users/andrewrichmond/Desktop/MacroIndicatorS-P/data/DATA.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

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
    
    return filtered_data


if __name__ == '__main__':
    data = data_load()
    data = preprocess(data)
    for i in range(10):
        print(data[i])