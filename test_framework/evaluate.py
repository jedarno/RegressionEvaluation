import numpy as np

from sklearn.model_selection import KFold
from sklearn.metrics import r2_score
from sklearn.utils import shuffle

from algorithms.least_squares_linear_regression import Least_squares
from algorithms.kernel_ridge import Kernel_ridge
from algorithms.svm import Svm
from algorithms.standard_scale import Standard_scale
from algorithms.knn import Knn

def cross_val(X, y, model, kernel_type=None, degree=5):
  """
  Performs 10 fold cross validation using a given modelal and data set and the coefficient of
  determination as the metric. Is called by the evaluate() function.

  Param X: The sample set as a numpy array

  Param y: The label set as a numpy array

  Param kernel_type: The kernel used, only required for models trained using a kernel

  Param degree: The degree parameter for polynomial kernels, has a default value of 3.
  """
  folds = KFold(n_splits=10)
  score = 0
  scores = []
  for train_index, test_index in folds.split(X, y):
    scaler = Standard_scale(X[train_index])
    X_train = scaler.normalise(X[train_index])
    X_test = scaler.normalise(X[test_index])
    
    if kernel_type != None:
      _model = model(X_train, y[train_index], kernel=kernel_type, degree=degree)

    else:
      _model = model(X_train, y[train_index])

    _pred = _model.predict(X_test)
    score = r2_score(y[test_index], _pred)
    scores.append(score)

  return scores
  
def evaluate(X, y, ridge_selected=False, lsqr_selected=False, svm_selected = False, knn_selected = False,\
  kernel='linear', d=3):
  """
  Evaluates the performance of the selected regression algorithms. Data is shuffled and normalised before 
  performing tests.

  Param X: The sample set being used in this 
  """
  names = []
  scores = []

  X, y = shuffle(X, y, random_state=1)
  if ridge_selected:
    print("Generating and testing Ridge model")
    ridge_score = cross_val(X, y, Kernel_ridge, kernel, degree=d)
    scores.append(ridge_score)
    names.append("Ridge")
    print("Ridge finished, score: ", np.mean(ridge_score))

  if lsqr_selected:
    print("Generating and testing OLS model...")
    lsqr_score =  cross_val(X, y , Least_squares)
    scores.append(lsqr_score)
    names.append("Least squares")
    print("OLS completed, score ",np.mean(lsqr_score))

  if svm_selected:
    print("Generating and testing SVR model...")
    svm_score = cross_val(X, y, Svm, kernel, d)
    scores.append(svm_score)
    names.append("SVR")
    print("SR completed, score ", np.mean(svm_score))

  if knn_selected:
    print("Generating and testing KNN model...")
    knn_score = cross_val(X, y, Knn)
    scores.append(knn_score)
    names.append("KNN")
    print("KNN completed, score: ", np.mean(knn_score))

  return names, scores


