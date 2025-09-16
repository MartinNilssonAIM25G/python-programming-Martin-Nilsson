import csv

def load_data_from_file():
    data_lines = []
    try:
        with open('datapoints.txt') as csv_file:
            data_lines = list(csv.reader(csv_file, delimiter=","))
    except FileNotFoundError:
        print("The file datapoints.txt does not exist") 
        return []
    return data_lines           
        
def parse_data(data_lines):
    features = []
    labels = []
    skipped_rows = []
    for row in data_lines:
            try:
                features.append([float(row[0]), float(row[1])])
                labels.append(int(row[2]))
            except ValueError:
                skipped_rows.append(row)
                continue
    return features, labels, skipped_rows            

def main():
    data_lines = load_data_from_file()
    features, labels, skipped_rows = parse_data(data_lines)

    print("Features:")
    for f in features:
        print(f)

    print("Labels:")
    print(labels)

    print("Skipped rows:")
    for row in skipped_rows:
        print(row)

if __name__ == "__main__":
    main()