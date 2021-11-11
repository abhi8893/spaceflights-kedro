from typing import Dict
import pandas as pd
from typing import Dict
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import logging

def split_data(data: pd.DataFrame, parameters: Dict)-> pd.DataFrame:
    '''Splits the data into feature and target training and test sets'''

    X, y = data[parameters['features']], data['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                            test_size=parameters['test_size'], 
                                            random_state=parameters['random_state'])
    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series)-> LinearRegression:
    '''Trains a linear regression model'''
    regressor = LinearRegression()
    return regressor.fit(X_train, y_train)


def evaluate_model(regressor: LinearRegression, X_test: pd.DataFrame, y_test: pd.Series):
    '''Calculates and logs the coefficient of determination for the linear regression model'''
    y_pred = regressor.predict(X_test)
    score = r2_score(y_test, y_pred)
    logger = logging.getLogger(__name__)
    logger.info('Model has a coefficient R^2 of %.3f on test_data', score)
    