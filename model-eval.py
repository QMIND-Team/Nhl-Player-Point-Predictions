# This file contains functions used to evaluate a model outputs

from keras.models import Sequential
from keras.layers import Dense
from keras.utils.vis_utils import plot_model
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


##get the accuracy of the model
def get_accuracy(NN_model, test, target):
    prediction = NN_model.predict(test)
    mse = 0
    for i in range(len(target)):
        mse += ((target.loc[i] - prediction[i]) ** 2)

    mse = mse / len(target)
    return 100 - mse.Target * 100

#Saves to a file the model input.
# Includes: shape, number of layers, parameters
def plot_model(model, to_file=, show_shapes=True, show_layer_names=True):
    plot_model(model, to_file=to_file, show_shapes=show_shapes, show_layer_names=show_layer_names)

# Visualize the results of different models
# I included some example code from a tutorial to work off of
def plot_results():

    '''
    # Visualise the Results of Polynomial Regression
plt.scatter(xtrain, ytrain, color = ‘red’)
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = ‘blue’)
plt.title(‘Polynomial Regression’)
plt.xlabel(‘Position level’)
plt.ylabel(‘Salary’)
plt.show()

# Visualise the Results of Polynomial Regression with Smoother Curve
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = ‘red’)
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = ‘blue’)
plt.title(‘Polynomial Regression’)
plt.xlabel(‘Position level’)
plt.ylabel(‘Salary’)
plt.show()
    '''