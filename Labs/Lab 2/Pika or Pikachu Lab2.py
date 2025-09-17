import matplotlib.pyplot as plt
import math

DATA_PATH = "datapoints.txt"
TEST_PATH = "testpoints.txt"

def load_data_from_file(filename):
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"The file {filename} does not exist")
        return []           
        
def parse_data(data_lines, test=False):
    features = []
    labels = []
    skipped_rows = []

    for row in data_lines:
        try:
            row = row.strip()
            if test:
                start = row.index("(")
                end = row.index(")")
                width_str, height_str = row[start+1:end].split(",")
                features.append([float(width_str.strip()), float(height_str.strip())])
            else:
                width_str, height_str, label_str = row.split(",")
                features.append([float(width_str), float(height_str)])
                labels.append(int(label_str))
        except Exception:
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
    # Real data
    train_lines = load_data_from_file(DATA_PATH)
    features, labels, skipped = parse_data(train_lines)
    plot_data(features, labels)

    # Test data
    test_lines = load_data_from_file(TEST_PATH)
    test_features, _, skipped_test = parse_data(test_lines, test=True)
    print(f"Test points: {test_features}")
    print(f"Skipped rows (test): {skipped_test}")
    

if __name__ == "__main__":
    main()