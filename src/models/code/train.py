# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import joblib
import os

# print("Current Working Directory:", os.getcwd())
data_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',"..","data"))
data_file = os.path.join(data_directory, 'hiring.csv')
dataset = pd.read_csv(data_file)

x = dataset.iloc[:, :3]
y = dataset.iloc[:, -1]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
def train_handler():
    """
    Trains a linear regression model using the provided training data.

    Parameters:
        None

    Returns:
        None
    """
    regressor = LinearRegression()
    # #Fitting model with trainig data
    regressor.fit(x, y)

    # Saving model to disk
    model_output_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',"output"))
    model_output_file =  os.path.join(model_output_directory, 'model.joblib')
    joblib.dump(regressor, model_output_file)


train_handler()
