# This file will containthe basic models we will use on our data.

from keras.callbacks import ModelCheckpoint
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from matplotlib import pyplot as plt
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore', category=DeprecationWarning)
from xgboost import XGBRegressor
from keras import models
from keras import layers

def checkpoint(name='checkpoint_default_name', monitor='val_loss', verbose=0, mode='auto'):
    checkpoint_name = name
    checkpoint = ModelCheckpoint(checkpoint_name, monitor=monitor, verbose=verbose, save_best_only=True, mode=mode)
    callbacks_list = [checkpoint]
    return callbacks_list

def DNN(df, activation, loss, input_layer=128, hidden_layers=256, kernel_initializer='normal', ):
    NN_model = Sequential()

    # Create the input layer
    NN_model.add(Dense(128, activation='relu', kernel_initializer='normal', input_dim=df.shape[1]))

    # Add hidden layers
    NN_model.add(Dense(256, activation='relu', kernel_initializer='normal'))
    NN_model.add(Dense(256, activation='relu', kernel_initializer='normal'))
    NN_model.add(Dense(256, activation='relu', kernel_initializer='normal'))

    # Add output layer
    NN_model.add(Dense(1, activation='linear', kernel_initializer='normal'))

    NN_model.compile(optimizer='adam', loss='mean_absolute_error', metrics=['mean_absolute_error'])

    # NN_model.summary()
    return NN_model

def get_accuracy(NN_model, test, target):
    prediction = NN_model.predict(test)
    mse = 0
    for i in range(len(target)):
        mse += ((target.loc[i] - prediction[i]) ** 2)

    mse = mse / len(target)
    return 100 - mse.Target * 100

## Willem
## define a function to create a linear regression model

def linear_regression_NN(initial_layers, training_data):
    lr_model = models.Sequential()

    ## add layers - assumed two hidden layers (more can be added/taken)
    lr_model.add(layers.Dense(initial_layers, activation='relu', input_shape=(training_data.shape[1], 1)))
    lr_model.add(layers.Dense(initial_layers, activation='relu'))

    ## add output_layer
    lr_model.add(layers.Dense(1))

    ## compile model, metric is mean absolute error (average distance between target and prediction)
    lr_model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    return lr_model


##Willem
##define a function which takes linear regression model, fits it to training data, then trains it with test
##to return the mae score of the test data (mean absolute error)

def train_LR_model(initial_layers, training_data, num_epochs, num_batches, training_targets, test_data, test_targets):

    ## call previous function to create neural network
    lr_model = linear_regression_NN(initial_layers, training_data)

    ## fit model to training data
    lr_model.fit(training_data, training_targets, epochs= num_epochs, batch_size=num_batches, verbose=0)

    test_mse_score, test_mae_score = lr_model.evaluate(test_data, test_targets)

    return test_mae_score






