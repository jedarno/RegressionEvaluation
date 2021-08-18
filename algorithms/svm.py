from sklearn.svm import SVR

class Svm:
  """
  Wrapper class, acts as an adapter for the sklearn class SVR()
  """
  def __init__(self, X, y, param=1, kernel='linear', degree=3):
    """
    param X: The training samples

    param y: The training labels

    param param: the value given as the paramater C, 
  	"""
    self.svm = SVR(C=param, kernel=kernel, degree=degree)
    self.svm.fit(X,y)

  def predict(self, X_test):
    return self.svm.predict(X_test)
