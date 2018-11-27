# This file contains all of the data visualization functions required for our data analysis.
# Functions include graphing, plotting, etc.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# For each graphing function, it should take in a df as the independent variable and have the option of graphing
# a new graph for each var or graphing them all on the same graph.

# can show correlations in data
def scatter_plot(X_var, Y_var, colour, x_label, y_label, title):
    plt.scatter(Y_var, X_var, c=colour, marker='.')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
    return

# distribution function
def histogram(X_var, Y_var, x_label, y_label, title):
    return 0

# good to visualize the rnage of an attribute
def boxplot(X_var, Y_var, x_label, y_label, title):
    return 0

