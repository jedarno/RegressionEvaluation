import unittest
from sklearn.datasets import load_boston
from sklearn.linear_model import Ridge as Sci_ridge
from sklearn.model_selection import train_test_split
import numpy as np

from ridge import Ridge
from standard_scale import Standard_scale

"""
Test class for ridge regression proof of concept class
"""
class Test_ridge(unittest.TestCase):

  def setUp(self):
    X, y = load_boston(return_X_y = True)
    X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=402060)

    scaler = Standard_scale(X_train)
    X_train = scaler.normalise(X_train)
    X_test = scaler.normalise(X_test)

    self.scikit_ridge = Sci_ridge(alpha=1)
    self.scikit_ridge.fit(X_train, y_train)
    self.X_test = X_test
    self.my_ridge = Ridge(X_train, y_train, 1)

  def test_coef(self):  
    my_coef = self.my_ridge.coefficient()
    their_coef = self.scikit_ridge.coef_
    for i in range(len(my_coef)):
        self.assertAlmostEqual(my_coef[i], their_coef[i], msg="Tests coefficient is correct.", places=5)

  def test_predict(self):
    my_y_pred = self.my_ridge.predict(self.X_test)
    their_y_pred = self.scikit_ridge.predict(self.X_test)
    for i in range(np.shape(self.X_test)[0]):
      self.assertAlmostEqual(my_y_pred[i], their_y_pred[i], msg="Tests predictions are similar to sklearn.", places=5)

  def test_tuning_parm(self):
    self.assertEqual(1, self.my_ridge.get_tuning_param(), msg="Tests tuning parameter used is returned by getter")
if __name__ == '__main__':
  unittest.main()
