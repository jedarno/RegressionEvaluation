import unittest
import numpy as np

from entry import Entry

class Test_entry(unittest.TestCase):
  def setUp(self):
    self.train = Entry('train.csv')
    self.train.set_feature_table(np.array(["on road old", "on road now","years", "km", "rating", "condition", "economy", "top speed", "hp", "torque"]))
    self.train.set_label("current price")
    
  def test_feature_shape(self):
    feature_table = self.train.get_feature_table()
    self.assertEqual(np.shape(feature_table), (10, 1000)) 
  
  def test_label_shape(self):
    labels = self.train.get_labels()
    self.assertEqual(np.shape(labels), (1000,))

  def test_get_columns(self):
    columns = self.train.get_columns()
    self.assertEqual(len(columns), 11)
    self.assertEqual(columns[0], "on road old")
if __name__ == '__main__':
  unittest.main()


