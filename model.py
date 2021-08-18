import numpy as np

from test_framework.evaluate import evaluate
from test_framework.entry import Entry
from no_features import No_features
from no_label import No_label
from sklearn.datasets import load_boston

class Model:
  """
  Class containing model object for mvc
  """
  def __init__(self):
    """
    Initialises model
    """
    self.data_added = False

  def run_evaluation(self, selected_ols, selected_ridge, selected_svr, selected_knn, features=None,\
     label=None, kernel="linear"):
    """
    Runs evaluation based on user selections
    """
    if self.data_added == False:
      self.X, self.y = load_boston(return_X_y = True)

    else:

      if features == None:
        raise No_features()

      if label == None:
        raise No_label()

      self.data_entry.set_feature_table(features)
      self.data_entry.set_label(label)
      self.X = self.data_entry.get_feature_table()
      self.y = self.data_entry.get_label()

    names, scores = evaluate(self.X, self.y, lsqr_selected=selected_ols, ridge_selected=selected_ridge,\
    svm_selected = selected_svr, knn_selected = selected_knn, kernel=kernel)
    avg_scores = np.zeros_like(names)
      
    for index, score in enumerate(scores):
      avg_scores[index] = np.mean(score)

    return names, scores, avg_scores

  def add_data(self, filename):
    self.data_entry = Entry(filename)

  def get_features(self):
    self.data_added =  True
    return self.data_entry.get_columns()

    
