# This file contains all of the data cleaning functions required for analyzing data.
# Functions include checking for null checks, removing/filling nulls, normalization, etc.

import pandas as pd
import numpy as np

# Takes in dataframe, calls functions and cleans data based on parameters
def cleaning(dataframe, nullThreshRow, nullThreshCol):
   return 0 #cleaned_df

# Remove rows in the data frame with nulls above the threshold
def remove_null_thresh_rows(dataframe, nullThreshRow):
    return 0 #new_df

# Remove columns in the data frame with nulls above the threshold
def remove_null_thresh_columns(dataframe, nullThreshCol):
    return  0 #new_df

# Count number of nulls in each row
def count_row_nulls(dataframe):
    return 0 #df with row and number of nulls

# Count number of nulls in each column
def count_column_nulls(dataframe):
    return 0 #df with column and number of nulls

# Fill a column with the median of the column
def fill_col_with_median(dataframe, colNum):
    return 0 #new_df

# Fill a column with the mean of the column
def fill_col_with_mean(dataframe, colNum):
    return 0 #new_df

# Find the median of a column
def find_median_of_col(dataframe, colNum):
    return 0 #float of median

# Find the mean of a column
def find_mean_of_col(dataframe, colNum):
    return 0 #float of mean

# Normalize given attributes (range() function is good)
def normalize(dataframe, attributes, 'min-max, z-score, etc', ):
    return 0 #new_df

def detect_outliers(dataframe):
    return 0

def remove_outliers():
    return 0