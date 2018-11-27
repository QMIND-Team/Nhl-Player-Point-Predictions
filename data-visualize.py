# This file contains all of the data visualization functions required for our data analysis.
# Functions include graphing, plotting, etc.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# For each graphing function, it should take in a df as the independent variable and have the option of graphing
# a new graph for each var or graphing them all on the same graph.

# can show correlations in data
def scatter_plot(X_var, Y_var, x_label, y_label, title):
    return 0

# distribution function
def histogram(column):
    plt.hist(column)

# good to visualize the range of an attribute
def boxplot(column):
    plt.boxplot(column)



