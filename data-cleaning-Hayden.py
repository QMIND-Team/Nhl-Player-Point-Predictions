# This file contains all of the data cleaning functions required for analyzing data.
# Functions include checking for null checks, removing/filling nulls, normalization, etc.

import pandas as pd
import numpy as np



# Takes in dataframe, calls functions and cleans data based on parameters
#Adam
def cleaning(dataframe, nullThreshRow, nullThreshCol):
   return 0 #cleaned_df

# Remove rows in the data frame with nulls above the threshold
#Willem
def remove_null_thresh_rows(dataframe, nullThreshRow):
    return 0 #new_df

# Remove columns in the data frame with nulls above the threshold
#Willem
def remove_null_thresh_columns(dataframe, nullThreshCol):
    return  0 #new_df

# Count number of nulls in each row
#Hayden
def count_row_nulls(dataframe):
    null_columns = dataframe.columns[dataframe.isnull().any()]
    print(dataframe[dataframe.isnull().any(axis=1)][null_columns].head())
    return 0 #df with row and number of nulls

# Count number of nulls in each column
#Hayden
def count_column_nulls(dataframe):
    null_columns = dataframe.columns[dataframe.isnull().any()]
    print(dataframe[null_columns].isnull().sum())
    return 0 #df with column and number of nulls

# Fill a column with the median of the column
#Hayden
def fill_col_with_median(dataframe, colName):
    dataframe[colName].fillna((dataframe[colName].median()), inplace=True)
    return dataframe

# Fill a column with the mean of the column
#hayden
def fill_col_with_mean(dataframe, colName):
    dataframe[colName].fillna((dataframe[colName].mean()), inplace=True)
    return dataframe

# Fill all null values with medians of respective columns
#hayden
def fill_all_median(dataframe):
    return dataframe.fillna(dataframe.median())

# Fill all null values with mean of respective columns
#hayden
def fill_all_mean(dataframe):
    return dataframe.fillna(dataframe.mean())

# Find the median of a column
#hayden
def find_median_of_col(dataframe, colName):
    return dataframe[colName].median()

# Find the mean of a column
#hayden
def find_mean_of_col(dataframe, colName):
    return dataframe[colName].mean

# Normalize given attributes (range() function is good)
#Andrew
#def normalize(dataframe, attributes, 'min-max, z-score, etc', ):
#    return 0 #new_df

#Ian
def detect_outliers(dataframe):
    return 0

#Ian
def remove_outliers():
    return 0

def main():
    #dataframe = pd.read_csv("train.csv")
    df = [['Alex', 0, None], ['Bob', 0, 12], ['Clarke', None, 13], ['Julia', 1, 14], ['Steven', 0, 1000], ['George', 0, 100]]
    dataframe = pd.DataFrame(df, columns=['Name', 'Gender', 'Age'], dtype=float)
    dataframe2 = pd.DataFrame(df, columns=['Name', 'Gender', 'Age'], dtype=float)
    count_column_nulls(dataframe)
    count_row_nulls(dataframe)
    print(fill_col_with_median(dataframe, 'Age').head())
    print(fill_col_with_mean(dataframe2, 'Age').head())
    print(fill_all_median(dataframe))
    print(fill_all_mean(dataframe2))
    print("Median of Gender is: ",find_median_of_col(dataframe,'Gender'))
    print("Mean of Age is: ", find_mean_of_col(dataframe2, 'Age'))

main()