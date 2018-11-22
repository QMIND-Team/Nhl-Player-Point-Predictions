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

# Fill all null values with median of respective columns
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
def normalize(dataframe, attributes, 'min-max, z-score, etc', ):
    return 0 #new_df

#Ian
def detect_outliers(df):
    outliers = []
    for column in df:
        cut_off = df[column].std() * 2
        lower = df[column].mean() - cut_off
        upper = df[column].mean() + cut_off
        row_count = 0
        for x in df[column]:
            if x >= upper or x <= lower:  # if below or above 2 stds from mean, add to outliers array
                outliers.append(row_count)  # adds row to outliers array
            row_count += 1
    outliers = list(set(outliers))  # removes duplicate rows
    return outliers

#Ian
def remove_outliers():
    outliers = detect_outliers(df)
    df = df.drop(index=outliers)
    return df

def get_col_with_no_nan(df, col_type):
    '''
    df - dataset to be checked
    col_type - num: columns containing only numerical data
               no_num: columns not containing numerical data
               any: all columns
    '''

    if col_type == 'num':
        predictors = df.select_dtypes(exclude=['object'])
    elif col_type == 'no_num':
        predictors = df.select_dtypes(include=['object'])
    elif col_type == 'any':
        predictors = df
    else:
        print('Please input a correct col_type value (num, no_num, any)')
        return 0

    col_with_no_nan = []
    for col in predictors.columns:
        if not df[col].isnull().any():
            col_with_no_nan.append(col)

    return col_with_no_nan
