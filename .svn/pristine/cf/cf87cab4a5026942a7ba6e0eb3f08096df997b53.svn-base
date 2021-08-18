import pandas as pd
import numpy as np

class Entry:
  """
  Class for taking user data and and providing it as numpy arrays for other classes to use.
  """
  def __init__(self, filename, index=0):
    """
    Initialises entry object, exports data from a csv file to a data frame and stores it as an attribute

    Param filename: The name of the file written 'filename.csv'

    Param index: the position of the index column in the csv
    """
    self.data = pd.read_csv(filename, index_col = index)
    
  def set_feature_table(self, features):
    """
    Selects the subset of columns selected as teh features and stores them as an attribute

    Param features: A list object containing the names of the features as strings.
    """
    samples_frame = self.data[features]
    self.samples = samples_frame.to_numpy()

  def set_label(self, label_col):
    """
    Selects the label column from the data frame and stores it as an a attribute.

    Param lavbel_col: The name fo the label column as a string
    """
    labels_frame = self.data[label_col]
    self.label = labels_frame.to_numpy()

  def get_feature_table(self):
    print(np.shape(self.samples))
    return self.samples

  def get_label(self):
    print(np.shape(self.label))
    return self.label
    
  def get_columns(self):
    return self.data.columns

