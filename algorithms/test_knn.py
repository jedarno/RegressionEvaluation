import numpy as np
import unittest
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

from knn import Knn
from knn import l2_dist

class Test_knn(unittest.TestCase):

  def test_l2_dist1(self):
    coord1 = [1,2]
    coord2 = [1,1]
    dist = l2_dist(coord1, coord2)
    self.assertEqual(dist, 1, "Tests euclidian distance is found correctly")

  def test_l2_disst2(self):
    coord1 = [1,1,1,1]
    coord2 = [4,4,4,4]
    dist = l2_dist(coord1, coord2)
    self.assertEqual(dist, 6, "Tests distance is found correctly with more dimesions")

  def test_get_label(self):
    knn = Knn([],[1,2,2,3],2)
    label = knn.get_label([0,1,2,3])
    self.assertEqual(label, 2, "Tests the label is calculated as mean of nearest labels")

  def test_find_k_nearest_neighbours(self):
    knn = Knn([[1,1],[9,9],[2,2],[5,5]], [1,1,1,1] , 2)
    knn_index = knn.find_k_nearest_neighbours([1,2])
    self.assertEqual(knn_index[0], 0, "Check first nn is found correctly.")
    self.assertEqual(knn_index[1], 2, "Check second nn is found correctly") 
    
  def test_predict_1(self):
    X_train = np.array([[2,2],[1,1],[9,9],[29,29],[10,10]])
    y_train = np.array([4,2,18,58,20])
    X_test = np.array([[1,2]])
    knn = Knn(X_train, y_train, 2)
    label = knn.predict(X_test)
    self.assertEqual(label[0], 3, "Tests the correct label is found")

  def test_get_k(self):
    knn = Knn([],[],235)
    self.assertEqual(knn.get_k(), 235)

  def test_no_k(self):
    X_train = np.array([[1,2],[1,3],[1,4],[2,2],[3,4],[3,2],[6,6]])
    y_train = np.array([4,2,18,58,20,90,12])
    X_test = [[1,2]]
    knn = Knn(X_train, y_train)
    knn.predict(X_test)
    self.assertIsNotNone(knn.get_k(), "Tests when None value is passed to K, a value is assigned.") 

  def test_large_dataset(self):
    X,y = load_boston(return_X_y = True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 1)
    knn = Knn(X_train, y_train)
    knn.predict(X_test)

if __name__ == '__main__':
  unittest.main()


