import numpy as np
import pandas as pd
from numpy.random import seed

# I made a new file so i could test the outliers function with a array of randomly generated numbers.
# this function is meant to calculate lower and upper bounds separating outliers for each category.
# then check if each value is outside those bounds.
# if they are, then they get added to an outliers array which gets returned
def detect_outliers(df):
    outliers = []
    vals = df.values
    for x in range(len(vals)):
        cut_off = df.std() * 2  # cut off is 2 standard deviations away from the mean
        lower = df.mean - cut_off
        upper = df.mean + cut_off
        for y in range(len(vals[x])):
            if y >= upper or y <= lower: # if below or above 2 stds from mean, add to outliers array
                outliers.append(y)
    return outliers

seed(1)
data = np.random.rand(300,42) # generates 300x42 array of random numbers to test function
data = pd.DataFrame(data)
print(detect_outliers(data))