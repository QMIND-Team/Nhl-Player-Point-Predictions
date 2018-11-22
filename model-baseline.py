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