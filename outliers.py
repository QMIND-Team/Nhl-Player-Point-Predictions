import numpy as np
import pandas as pd
from numpy.random import seed

# I made a new file so i could test the outliers function with a array of randomly generated numbers.
# this function is meant to calculate lower and upper bounds separating outliers for each category.
# then check if each value is outside those bounds.
# if they are, then they get added to an outliers array which gets returned
def detect_outliers(df):
    outliers = []
    for column in df:
        df[column]
        cut_off = df[column].std()
        lower = df[column].mean() - cut_off
        upper = df[column].mean() + cut_off
        row_count = 0
        for row in df[column]:
            if row >= upper or row <= lower: # if below or above 2 stds from mean, add to outliers array
                outliers.append((column, row_count))
            row_count += 1
    return outliers

seed(1)
data = np.random.rand(300,42) # generates 300x42 array of random numbers to test function
data = pd.DataFrame(data)
print(detect_outliers(data))