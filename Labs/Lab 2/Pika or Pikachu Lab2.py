import csv
import matplotlib.pyplot as plt
import math

def load_data_from_file(filename):
    data_lines = []
    try:
        with open(filename) as csv_file:
            data_lines = list(csv.reader(csv_file, delimiter=","))
    except FileNotFoundError:
        print(f"The file {filename} does not exist") 
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

def plot_data(features, labels):
    x_points = [width for width, height in features]
    y_points = [height for width, height in features]
    distance = [math.sqrt(x_points[i]**2 + y_points[i]**2) for i in range(len(features))]
    colors = ['green' if label == 0 else 'black' for label in labels]

    plt.title("Pica or Pikachu Lab 2")
    plt.scatter(x_points, y_points, c=colors)
    plt.show()


def main():
    data_lines = load_data_from_file("datapoints.txt")
    features, labels, skipped_rows = parse_data(data_lines)
    plot_data(features, labels)

if __name__ == "__main__":
    main()