# program that uses NumPy to calculate basic statistical measures
# (mean, median, and standard deviation) for a given dataset:
import numpy as np 

def calculate_stats(data):
    mean_val = np.mean(data)
    median_val = np.median(data)
    std_dev_val = np.std(data)

    return mean_val,median_val,std_dev_val

if __name__ == "__main__":
    # sample dataset
    dataset = np.array([23, 45, 67, 12, 56, 34, 78, 90, 43, 21])

    # stats calculation
    mean, median, std_deviation = calculate_stats(dataset)

    # Output
    print(f"Given Dataset is {dataset}")
    print(f"Mean is {mean:.2f}")
    print(f"Median is {median}")
    print(f"Standard Deviation is {std_deviation: .2f}")


