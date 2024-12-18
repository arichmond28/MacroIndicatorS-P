import csv

def data_load():
    with open('/Users/andrewrichmond/Desktop/MacroIndicatorS-P/data/DATA.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


if __name__ == '__main__':
    data = data_load()
    for i in range(10):
        print(data[i])