import numpy as np
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score

"""
A class for creating a linear model that uses ridge regression.
"""
class Ridge:

  """
  Initialiser takes training samples, labels and a tuning parameter to produce a model on which
  predictions can use.

  param X_train: A numpy array containing the matrix of training samples.

  param y_train: A numpy array containg the taining labels.

  tuning_param: The tuning parameter, used as a scaler in the shrinkage penalty. If not provided
    the default in None, and a value will be found using cross validation.
  """
  def __init__(self, X_train, y_train, tuning_param=1):

    i_matrix = np.identity(np.shape(X_train)[1])

    self.X_train = X_train
    self.y_train = y_train

    if tuning_param == None:
      tuning_param = self.find_tuning_param()
     
    _XT = X_train.T
    _XT_y = np.matmul(_XT, y_train)
    _XT_X = np.matmul(_XT, X_train)
    _alpha_I = tuning_param * i_matrix
    _XT_X_plus_alpha = np.add(_XT_X, _alpha_I)
    _inv_bracket = np.linalg.inv(_XT_X_plus_alpha)

    self.coef = np.matmul(_XT_y, _inv_bracket)
    self.tuning_param = tuning_param
  """
  Function to find the ideal tuning parameter if the user has not specified a value. 
  """
  def find_tuning_param(self):
    best_score = np.NINF
    alphas = [0, 0.001, 0.01, 0.1, 1, 10, 100, 1000]
    folds = KFold(n_splits=5, shuffle=True)
    best_alpha = alphas[0]
    for alpha in alphas:
      total_score = 0
      for train_index, test_index in folds.split(self.X_train, self.y_train):
        trial_model = Ridge(self.X_train[train_index], self.y_train[train_index], tuning_param = alpha)
        trial_pred = trial_model.predict(self.X_train[test_index])
        total_score += r2_score(self.y_train[test_index], trial_pred)
      avg_score = total_score/5
      if avg_score > best_score:
        best_score = avg_score
        best_alpha = alpha        
    return best_alpha

  """
  Returns the coefficient of the linear model.

  Returns: numpy array of floats of the coefficient of each feature.
  """
  def coefficient(self):
    return self.coef

  """
  Returns the value of the tuning parameter Alpha.
  """
  def get_tuning_param(self):
    return self.tuning_param
  """
  Predicts the y values of a numpy array of samples.

  Returns: A  numpy array containg floats of the label prediction for each sample.
  """
  def predict(self, X_test):
    hat = np.matmul(X_test, self.coef)
    hat += np.mean(self.y_train)
    return hat

    
