import numpy as np
import pandas as pd


# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))


# k-Nearest Neighbors algorithm
def knn(data, query, k):
    distances = []

    for index, row in data.iterrows():
        distance = euclidean_distance(row[:-1].values, query)
        distances.append((distance, row[-1]))

    distances.sort(key=lambda x: x[0])

    neighbors = [dist[1] for dist in distances[:k]]
    return neighbors


# Prepare the dataset
data = pd.DataFrame([
    [158, 58, 'M'],
    [158, 59, 'M'],
    [158, 63, 'M'],
    [160, 59, 'M'],
    [160, 60, 'M'],
    [163, 60, 'M'],
    [163, 61, 'M'],
    [160, 64, 'L'],
    [163, 64, 'L'],
    [165, 61, 'L'],
    [165, 62, 'L'],
    [165, 65, 'L'],
    [168, 62, 'L'],
    [168, 63, 'L'],
    [168, 66, 'L'],
    [170, 63, 'L'],
    [170, 64, 'L'],
    [170, 68, 'L']
], columns=['Height', 'Weight', 'TshirtSize'])

# Predict the T-shirt size for the new customer using k=3
query = np.array([161, 61])
k = 3
neighbors = knn(data, query, k)
prediction = max(set(neighbors), key=neighbors.count)
print(f"Prediction (k=3): {prediction}")
print(f"Neighbors (k=3): {neighbors}")

# Predict the T-shirt size for the new customer using k=5
k = 5
neighbors = knn(data, query, k)
prediction = max(set(neighbors), key=neighbors.count)
print(f"Prediction (k=5): {prediction}")
print(f"Neighbors (k=5): {neighbors}")
