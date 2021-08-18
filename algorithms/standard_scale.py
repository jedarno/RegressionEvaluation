import numpy as np

"""
Class to scale data, by moving the mean to 0 and the standard deviation to 1.
"""
class Standard_scale:

  """
  Initialiser calculates and stores the mean and standard deviation of data given.

  param X: A numpy array containing data to be normalised. If using training and test set,
    this should be your training set. 
  """
  def __init__(self, X):
    self.X_mean = np.mean(X, axis = 0)
    self.X_sd = np.std(X, axis = 0)


  """
  Normalises a dataset to the scale calculated when initialising, this is done seperately so that
  the training and test set can be scaled by the same values.

  param X: A numpy array contianing the data to be normalised.
  """
  def normalise(self, X):
    X_norm = np.copy(X)
    X_norm = X_norm - self.X_mean
    X_norm = X_norm / self.X_sd

    return X_norm


