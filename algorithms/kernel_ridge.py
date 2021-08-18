import numpy as np

from sklearn.model_selection import KFold
from sklearn.metrics import r2_score

from algorithms.kernels import kernel_function


class Kernel_ridge:
  """
  A class for creating a linear model that uses ridge regression.
  """

  
  def __init__(self, X_train, y_train, tuning_param=None, kernel='linear', r=1, degree=2):
    """
    Initialiser takes training samples, labels and a tuning parameter to produce a model on which
    predictions can use.

    param X_train: A numpy array containing the matrix of training samples.

    param y_train: A numpy array containg the taining labels.

    tuning_param: The tuning parameter, used as a scaler in the shrinkage penalty. If not provided
      the default in None, and a value will be found using cross validation.
    """
    self.kernel = kernel
    self.d  = degree

    i_matrix = np.identity(np.shape(X_train)[0])
    self.X_train = X_train
    self.y_train = y_train

    if tuning_param == None:
      tuning_param = self.find_tuning_param()

    self.k = kernel_function(X_train, X_train, kernel, d = degree)
    _lambda = tuning_param * i_matrix
    k_plus_lambda = np.add(self.k, _lambda)
    inv_k_plus_lambda = np.linalg.inv(k_plus_lambda)
    inv_brackets_y = np.matmul(inv_k_plus_lambda, y_train)
    
    self.alpha = inv_brackets_y

  
  def find_tuning_param(self):
    """
    Function to find the ideal tuning parameter if the user has not specified a value. 

    Return: The tuning parameterthat provides the highest score 
    """
    best_score = np.NINF
    alphas = [0.01, 0.1, 1, 10, 50, 100, 250, 500, 750, 1000]
    folds = KFold(n_splits=5, shuffle=True)

    for alpha in alphas:
      total_score = 0
      for train_index, test_index in folds.split(self.X_train, self.y_train):
        trial_model = Kernel_ridge(self.X_train[train_index], self.y_train[train_index], tuning_param = alpha)
        trial_pred = trial_model.predict(self.X_train[test_index])
        total_score += r2_score(self.y_train[test_index], trial_pred)
      avg_score = total_score/5

      if avg_score > best_score:
        best_score = avg_score
        best_alpha = alpha        
    return best_alpha

  
  def alpha(self):
    """
    Returns the coefficient of the linear model.

    eturns: numpy array of floats of the coefficient of each feature.
    """
    return self.alpha

  
  def predict(self, X_test):
    """
    Predicts the y values of a numpy array of samples.

    Returns: A  numpy array containg floats of the label prediction for each sample.
    """
    hat = np.matmul(self.alpha, kernel_function(X_test, self.X_train, self.kernel, d=self.d).T)

    if self.kernel == 'linear':
      hat += np.mean(self.y_train)

    return hat

    
