import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

def main():
    print("Welcome to my Python project!")

    # Test numpy
    array = np.array([1, 2, 3, 4, 5])
    print("Numpy array:", array)

    # Test pandas
    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
    df = pd.DataFrame(data)
    print("Pandas DataFrame:")
    print(df)

    # Test matplotlib
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.title("Matplotlib Test Plot")
    plt.show()

    # Test scipy
    result = stats.ttest_1samp(array, 3)
    print("Scipy t-test result:", result)

if __name__ == "__main__":
    main()
