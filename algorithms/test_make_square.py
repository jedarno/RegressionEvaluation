import unittest
import numpy as np

from make_square import make_square

class Test_make_square(unittest.TestCase):
  
  def test_makes_square(self):
    X = np.array([[1,1,1],[2,2,2]])
    X = make_square(X)
    r,c = np.shape(X)
    self.assertEqual(r, c, "Tests rows and columns are made equal")

  def test_makes_square2(self):
    X = np.array([[1,1],[1,1],[1,1]])
    X = make_square(X)
    r, c = np.shape(X)
    self.assertEqual(r, c, "Tests columns of zeroes added to make square")

  def test_takes_square(self):
    X = np.array([[1,1],[2,2,]])
    X = make_square(X)
    r,c = np.shape(X)
    self.assertEqual(r, c, "Tests a square array is returned unchanged")

  def test_large_dataset_less_rows(self):
    X = np.full((10,100),1)
    X = make_square(X)
    r,c = np.shape(X)
    self.assertEqual(r,c, "tests a  large matrix with more columns than rows is made square")

  def test_large_dataset_less_columns(self):
    X = np.full((100,10),1)
    X = make_square(X)
    r,c = np.shape(X)
    self.assertEqual(r,c, "tests a  large matrix with more rows than columns is made square")

if __name__ == '__main__':
  unittest.main()
