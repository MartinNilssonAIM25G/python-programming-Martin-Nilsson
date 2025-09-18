import matplotlib.pyplot as plt
import numpy as np

DATA_PATH = "datapoints.txt"
TEST_PATH = "testpoints.txt"

def load_data_from_file(filename: str) -> list[str]:
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"The file {filename} does not exist")
        return []           

def get_valid_float(prompt: str, min_value: float | None = None) -> float:
    while True:
        try:
            f = float(input(prompt).strip())
            if (min_value is not None and f <= min_value):
                print(f"Please enter a positive number")
                continue
            return f
        except ValueError:
            print("Please enter a valid number.")

def fetch_user_input() -> tuple[float, float]:
    user_width = get_valid_float("Enter the width of the Pokemon (in cm): ", 0)
    user_height = get_valid_float("Enter the height of the Pokemon (in cm): ", 0)
    return (user_width, user_height)

def parse_data(data_lines: list[str], test: bool = False) -> tuple[list[list[float]], list[int], list[str]]:
    features = []
    labels = []
    skipped_lines = []

    for line in data_lines:
        try:
            row = line.strip()
            if test:
                start = line.index("(")
                end = line.index(")")
                width_str, height_str = line[start+1:end].split(",")
                features.append([float(width_str.strip()), float(height_str.strip())])
            else:
                width_str, height_str, label_str = line.split(",")
                features.append([float(width_str), float(height_str)])
                labels.append(int(label_str))
        except ValueError:
            skipped_lines.append(line)
            continue

    return features, labels, skipped_lines             

def plot_data(features: list[list[float]], labels: list[int]) -> None:
    x_points = [width for width, height in features]
    y_points = [height for width, height in features]
    colors = ['green' if label == 0 else 'black' for label in labels]

    plt.title("Pica or Pikachu Lab 2")
    plt.scatter(x_points, y_points, c=colors)
    plt.grid()
    plt.show()

def count_distance(point1: list[float], point2: list[float]) -> float:
    x, y = point1
    width, height = point2
    return np.sqrt(np.power(x - width, 2) + np.power(y - height, 2))

def test_classification(test_point: list[float], features: list[list[float]], labels: list[int]) -> str:

    result = ""
    lowest_distance = None
    
    for i, training_point in enumerate(features):
        distance = count_distance(test_point, training_point)
        if lowest_distance is None or distance < lowest_distance:
            lowest_distance = distance
            result = "Pikachu" if labels[i] == 1 else "Pichu"
    
    return result


def main() -> None:
    
    data_points = load_data_from_file(DATA_PATH) # Real data
    features, labels, skipped = parse_data(data_points)
    plot_data(features, labels)
   
    test_points = load_data_from_file(TEST_PATH) # Test data
    test_features, _, skipped_test = parse_data(test_points, test=True)

    for test_point in test_features:
        classification = test_classification(test_point, features, labels)
        print(f"Sample with (width, height): {test_point} classified as a {classification}")

    user_demensions = fetch_user_input()
    classification = test_classification(list(user_demensions), features, labels)
    print(f"User input (width, height): {user_demensions} classified as a {classification}")    
    

if __name__ == "__main__":
    main()