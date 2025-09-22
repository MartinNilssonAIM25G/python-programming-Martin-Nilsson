import matplotlib.pyplot as plt
import numpy as np
import collections
from typing import Optional
import random


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

def get_user_input() -> tuple[float, float]:
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

def plot_data_with_test(features: list[list[float]],labels: list[int],test_features: Optional[list[list[float]]] = None,test_labels: Optional[list[int]] = None,user_point: Optional[list[float]] = None,user_label: Optional[str] = None) -> None:
    x_train = [width for width, height in features]
    y_train = [height for width, height in features]
    colors_train = ['green' if label == 0 else 'black' for label in labels]
    plt.scatter(x_train, y_train, c=colors_train, label="Training data", s=50, alpha=0.6)

    if test_features is not None:
        x_test = [width for width, height in test_features]
        y_test = [height for width, height in test_features]
        if test_labels:
            colors_test = ['green' if label == 0 else 'black' for label in test_labels]
        else:
            colors_test = ['blue'] * len(test_features)
        plt.scatter(x_test, y_test, c=colors_test, marker='x', label="Test data", s=80)

    # Användarens input
    if user_point:
        plt.scatter(user_point[0], user_point[1], c='red', marker='*', s=200, label=f"User input: {user_label}")

    plt.title("Pica or Pikachu with Test Points")
    plt.xlabel("Width (cm)")
    plt.ylabel("Height (cm)")
    plt.grid(True)
    plt.legend()
    plt.show()

def count_distance(point1: list[float], point2: list[float]) -> float:
    x, y = point1
    width, height = point2
    return np.sqrt(np.power(x - width, 2) + np.power(y - height, 2))



def get_distance_entry(entry: tuple[float, int]) -> float:
    return entry[0]

def get_sorted_distances(test_point: list[float], features: list[list[float]], labels: list[int]) -> list[tuple[float, int]]:
    distances = [(count_distance(test_point, f), l) for f, l in zip(features, labels)]
    distances.sort(key=get_distance_entry)
    return distances

def get_nearest_neighbor(test_point: list[float], features: list[list[float]], labels: list[int]) -> str:
    sorted_distances = get_sorted_distances(test_point, features, labels)
    if not sorted_distances:
        return "Pichu"
    return "Pikachu" if sorted_distances[0][1] == 1 else "Pichu"

def get_k_nearest_neighbors(test_point: list[float], features: list[list[float]], labels: list[int], k: int) -> Optional[str]:
    sorted_distances = get_sorted_distances(test_point, features, labels)
    if not sorted_distances:
        return "Pichu"

    k = min(k, len(sorted_distances))
    k_labels = [l for _, l in sorted_distances[:k]]

    counts = {label: k_labels.count(label) for label in set(k_labels)}
    max_votes = max(counts.values())
    candidates = [label for label, count in counts.items() if count == max_votes]

    classification_knn = random.choice(candidates)
    return "Pikachu" if classification_knn == 1 else "Pichu"


def main() -> None:
    random.seed(42)

    data_points = load_data_from_file(DATA_PATH) # Real data
    features, labels, skipped = parse_data(data_points)
   
    test_points = load_data_from_file(TEST_PATH) # Test data
    test_features, _, skipped_test = parse_data(test_points, test=True)

    for test_point in test_features:
        classification = get_nearest_neighbor(test_point, features, labels)
        print(f"Sample with (width, height): {test_point} classified as a {classification}")

    user_dimensions = get_user_input()
    user_class_nn = get_nearest_neighbor(list(user_dimensions), features, labels)
    user_class_knn = get_k_nearest_neighbors(list(user_dimensions), features, labels, 10)
    print(f"User input (width, height): {user_dimensions} classified as a {user_class_nn}\nIf we instead look at the nearest 10 neighbours it's classified as {user_class_knn}, was it classified as the same?")    
    
    plot_data_with_test(features, labels,test_features=test_features, user_point=list(user_dimensions), user_label=user_class_knn)

if __name__ == "__main__":
    main()