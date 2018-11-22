# This file contains all of the data cleaning functions required for analyzing data.
# Functions include checking for null checks, removing/filling nulls, normalization, etc.

import pandas as pd
import numpy as np

import pandas as pd
from scipy.stats import zscore
from sklearn.preprocessing import minmax_scale
from sklearn.preprocessing import power_transform
from sklearn.preprocessing import quantile_transform

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
def normalize(dataframe, type ):
    global normalized_data
    if type == zscore:
        clean_data = dataframe.select_dtypes(['number'])
        cleaner_data = clean_data.dropna(how='any')
        normalized_data = cleaner_data.apply(zscore)
    elif type == minmax:
        clean_data = dataframe.select_dtypes(['number'])
        cleaner_data = clean_data.dropna(how='any')
        minmax_data = minmax_scale(cleaner_data)
        normalized_data = pd.DataFrame(minmax_data)
    elif type == l1_norm:
        clean_data = dataframe.select_dtypes(['number'])
        cleaner_data = clean_data.dropna(how='any')
        norm_data = normalize(cleaner_data, norm='l1')
        normalized_data = pd.DataFrame(norm_data)
    elif type == l2_norm:
        clean_data = dataframe.select_dtypes(['number'])
        cleaner_data = clean_data.dropna(how='any')
        norm_data = normalize(cleaner_data, norm='l2')
        normalized_data = pd.DataFrame(norm_data)
    elif type == power_yeo:
        clean_data = dataframe.select_dtypes(['number'])
        cleaner_data = clean_data.dropna(how='any')
        power_data = power_transform(cleaner_data, method='yeo-johnson')
        normalized_data = pd.DataFrame(power_data)
    elif type == power_box:
        clean_data = dataframe.select_dtypes(['number'])
        cleaner_data = clean_data.dropna(how='any')
        power_data = power_transform(cleaner_data, method='box-cox')
        normalized_data = pd.DataFrame(power_data)
    elif type == quantile:
        clean_data = dataframe.select_dtypes(['number'])
        cleaner_data = clean_data.dropna(how='any')
        quantile_data = quantile_transform(cleaner_data)
        normalized_data = pd.DataFrame(quantile_data)
    return normalized_data

#Ian
def detect_outliers(dataframe):
    return 0

#Ian
def remove_outliers():
    return 0

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
