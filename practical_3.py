import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# Load Iris flower dataset
iris = load_iris()

X = iris.data
y = iris.target


# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# Apply PCA and reduce dimensions to 2
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)


# Display explained variance
print("Original Data Shape:", X.shape)
print("Reduced Data Shape:", X_pca.shape)

print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)

print("\nTotal Explained Variance:",
      np.sum(pca.explained_variance_ratio_))


# Plot all three classes
plt.figure(figsize=(8, 6))

for class_value, class_name in enumerate(iris.target_names):
    plt.scatter(
        X_pca[y == class_value, 0],
        X_pca[y == class_value, 1],
        label=class_name
    )

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("Iris Dataset after PCA")
plt.legend()
plt.grid(True)

plt.show()