import numpy as np
import matplotlib.pyplot as plt
from statistics import multimode


# Given datasets
X1 = [1, 2, 3, 4, 5, 4, 3, 2, 4, 5,
      1, 2, 3, 4, 2, 5, 1, 3, 2, 1,
      2, 1, 1, 1, 2]

X2 = [1, 2, 3, 4, 5, 4, 3, 2, 4, 5,
      1, 2, 3, 4, 2, 5, 1, 3, 2, 1,
      2, 1, 1, 1, 2000]

X3 = [1, 2, 3, 10, 20, 30, 100, 200,
      300, 1000, 2000, 3000]


def calculate_statistics(data):
    mean = np.mean(data)
    median = np.median(data)
    mode = multimode(data)

    return mean, median, mode


datasets = {
    "X1": X1,
    "X2": X2,
    "X3": X3
}


# Calculate and display results
print("Mean, Median and Mode")
print("-" * 40)

for name, data in datasets.items():
    mean, median, mode = calculate_statistics(data)

    print(f"\n{name}")
    print(f"Mean   : {mean}")
    print(f"Median : {median}")
    print(f"Mode   : {mode}")


# Histogram for X1
mean = np.mean(X1)
median = np.median(X1)
mode = multimode(X1)[0]

plt.hist(X1, bins=np.arange(0.5, 6.5, 1), edgecolor="black")

plt.axvline(mean, label=f"Mean = {mean}")
plt.axvline(median, label=f"Median = {median}")
plt.axvline(mode, label=f"Mode = {mode}")

plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram of X1")
plt.legend()

plt.show()