import numpy as np
import matplotlib.pyplot as plt

# Datasets given in the lab manual
X1 = [1, 2, 3, 4, 5, 4, 3, 2, 4, 5,
      1, 2, 3, 4, 2, 5, 1, 3, 2, 1,
      2, 1, 1, 1, 2]

X2 = [1, 2, 3, 4, 5, 4, 3, 2, 4, 5,
      1, 2, 3, 4, 2, 5, 1, 3, 2, 1,
      2, 1, 1, 1, 2000]

X3 = [1, 2, 3, 10, 20, 30, 100, 200,
      300, 1000, 2000, 3000]


def calculate_statistics(data):
    standard_deviation = np.std(data)
    variance = np.var(data)

    return standard_deviation, variance


datasets = {
    "X1": X1,
    "X2": X2,
    "X3": X3
}


print("Standard Deviation and Variance")
print("-" * 40)

for name, data in datasets.items():
    standard_deviation, variance = calculate_statistics(data)

    print(f"\n{name}")
    print(f"Standard Deviation : {standard_deviation}")
    print(f"Variance           : {variance}")


# Histogram data given in the lab manual
X = [1, 3, 2, 4, 56, 4, 3, 2, 4, 5,
     3, 1, 2, 3, 2, 3, 1, 4]

mean = np.mean(X)
standard_deviation = np.std(X)
variance = np.var(X)

plt.hist(X, bins=10, edgecolor="black")

plt.axvline(
    mean + standard_deviation,
    linestyle="--",
    label=f"Mean + SD = {mean + standard_deviation:.2f}"
)

plt.axvline(
    mean - standard_deviation,
    linestyle="--",
    label=f"Mean - SD = {mean - standard_deviation:.2f}"
)

plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram showing Standard Deviation and Variance")
plt.legend()

plt.show()