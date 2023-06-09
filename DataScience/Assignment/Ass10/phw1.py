
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans



# Load the dataset
dataset = np.loadtxt('mouse.csv', delimiter=',')

# Draw a scatter plot to visualize the dataset
plt.scatter(dataset[:, 0], dataset[:, 1])
plt.title("Initial Dataset")
plt.show()

# Define parameter combinations
clusters = [2, 3, 4, 5, 6]
iterations = [50, 100, 200, 300]

# Dictionary to store results
results = {}

# Run KMeans with varying parameters
for n_clusters in clusters:
    for max_iter in iterations:
        kmeans = KMeans(n_clusters=n_clusters, max_iter=max_iter, random_state=42)
        kmeans.fit(dataset)
        # Store the results
        results[(n_clusters, max_iter)] = kmeans.inertia_  # Inertia: Sum of distances of samples to their closest cluster center

# Sort results by inertia
sorted_results = sorted(results.items(), key=lambda item: item[1])

# Show the 3 best results for each number of clusters
best_results = {}
for n_clusters in clusters:
    cluster_results = [result for result in sorted_results if result[0][0] == n_clusters]
    best_results[n_clusters] = cluster_results[:3]

# Print the 3 best results for each number of clusters
for n_clusters, results in best_results.items():
    print(f"For {n_clusters} clusters:")
    for result in results:
        print(f"   Max_iter: {result[0][1]}, Inertia: {result[1]}")

# Run KMeans with the best parameters
best_parameters = sorted_results[0][0]
kmeans = KMeans(n_clusters=best_parameters[0], max_iter=best_parameters[1], random_state=42)
kmeans.fit(dataset)

# Draw a scatter plot to visualize the clustering result
plt.scatter(dataset[:, 0], dataset[:, 1], c=kmeans.labels_)
plt.title("Final Clustering Result")
plt.show()

# The reason of choosing 'best' result
# The reason to choose the 3 best results for each number of clusters is to explore the effects of different parameters on the clustering algorithm's performance for each possible cluster number. The 'best' in this context is defined by the inertia, which is the sum of squared distances of samples to their closest cluster center. A lower inertia value signifies a better clustering result, hence we sort the results based on inertia and pick the top 3.
#
# Finally, we choose a single best overall result to use for our final clustering. This is simply because at the end of the day, we want a single clustering solution to apply to our data. The final best parameters are chosen based on the same criterion: the lowest inertia. This best set of parameters gives us the most optimal clustering solution across all combinations of parameters we've tried. In the final step, we run the KMeans algorithm again with this best combination to produce our final clustering result.