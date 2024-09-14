import csv

def read_csv_file(file_path):
    with open(file_path, mode='r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            print(row)

if __name__ == "__main__":
    read_csv_file('W1 Well Logs.csv')
