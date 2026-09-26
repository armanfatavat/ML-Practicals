import numpy as np


# Vectors given in the lab manual
A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
B = np.array([1, 3, 5, 7, 9, 7, 5, 3, 1, 0])

X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Y = np.array([1, 3, 5, 7, 9, 7, 5, 3, 1, 0])


# Cosine similarity
def cosine_similarity(A, B):
    return np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))


# Euclidean distance
def euclidean_distance(A, B):
    return np.sqrt(np.sum((A - B) ** 2))


# Calculate measures
cosine_AB = cosine_similarity(A, B)
cosine_XY = cosine_similarity(X, Y)

euclidean_AB = euclidean_distance(A, B)
euclidean_XY = euclidean_distance(X, Y)


# Display results
print("Similarity and Dissimilarity Measures")
print("-" * 45)

print("\nCosine Similarity:")
print(f"(A, B) = {cosine_AB:.4f}")
print(f"(X, Y) = {cosine_XY:.4f}")

print("\nEuclidean Distance:")
print(f"(A, B) = {euclidean_AB:.4f}")
print(f"(X, Y) = {euclidean_XY:.4f}")