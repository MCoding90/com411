import csv

records = []
headings = []


def load_data(file_path):
    print("Loading data...", end="")

    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        headings = next(csv_reader)

        for line in csv_reader:
            records.append(line)

    print("Done!")