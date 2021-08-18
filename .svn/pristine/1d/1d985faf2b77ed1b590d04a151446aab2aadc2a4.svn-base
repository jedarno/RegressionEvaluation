import numpy as np

class Least_squares:
  """
  Class to implement a linear model using least squares regression.
  """
  
  

  def __init__(self, X_train, y_train):
    """
    Initialiser takes the training set, adds a column of ones to the start of
    the sample set so that it appears as the first feature. It then calculates
    the optimal Coefficient for each feature when applied to a linear model
    using least squares.

    Param X_train: A numpy array of training samples.

    Param y_train: A numpy array of the training labels.  
    """

    size_p_plus_1  = (np.shape(X_train)[0], np.shape(X_train)[1] + 1)
    self._X = np.ones(size_p_plus_1)
    self._X[:, 1:] = X_train
    self._y = y_train
   
    _XT = self._X.T
    _XTX = np.matmul(_XT, self._X)
    _inv_XTX = np.linalg.inv(_XTX)
    
    self.coef = np.matmul(np.matmul(_inv_XTX, _XT), self._y)

  
  def coefficient(self):
    """
    Returns the coefficients of the features.

    Return: numpy array of the coefficients of features. 
    """

    return self.coef[1:]

  
  def intercept(self):
    """
    Returns the intercept
    """
    return self.coef[0]

  def predict(self, X_test):
    """
    Takes a set of samples adds a column of ones in front of the features, then multiplies by
    the coefficient fittef to the training set to return the predicted labels.

    param X_test: Numpy array of samples.

    return: Numpy array of predicted values.
    """
    size_p_plus_1  = (np.shape(X_test)[0], np.shape(X_test)[1] + 1)
    X_prime = np.ones(size_p_plus_1)
    X_prime[:, 1:] = X_test
    hat = np.matmul(X_prime, self.coef)
    return hat    
    

