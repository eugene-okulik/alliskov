import csv


def read_data_from_csv(file_path):
    with open(file_path, newline='') as csv_file:
        file_data = csv.DictReader(csv_file)
        for line in file_data:
            yield line
