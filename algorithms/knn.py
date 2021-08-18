import numpy as np
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score

def l2_dist(coord1, coord2):

  """
  Finds the euclidian between two points.
  
  Param coord1 & coord2: The two points as numpy arrays or lists, can be of any length(e.g. points in a 4d space).

  Return: The euclidian distance as a float.
  """

  sum = 0
  for i in range(len(coord1)):
    sum += pow(coord1[i] - coord2[i], 2)

  return np.sqrt(sum)

class Knn:

  """
  Class to produce and make predictions on a K Nearest Neighbour regression model.
  """

  def __init__(self, X, y, k=None):
    """
    Stores X and y trainging data as class attributes. If k is not given, an optimal k is found.
    
    param X: numpy array of training samples

    param y: numpy array of training labels

    param k: optional parameter. The number of neighbours considered when findin predicted label.
    """
    self.X_train = X
    self.y_train = y

    if k == None:
      self.k = self.find_k()
    else:
      self.k = k

  def get_label(self, knn_index):

    """
    Function to find the label of a sample by averaging the labels of it's nearest neighbours.

    Param knn_index: The index locations offailed to push some refs to 'https://github.com/ the nearest neighbours in the training set.

    Return: The mean of the label values of the k nearest neighbours.
    """

    labels = np.zeros_like(knn_index)
    for i, knn_index in enumerate(knn_index):
      labels[i] = self.y_train[knn_index]
    
    return np.mean(labels)       

  def find_k_nearest_neighbours(self, test_sample):

    """
    For a given sample, finds the closest points by l2 distance  within the training set.
  
    Param test_sample: The sample being evaluated

    Return: A numpy array of the inexes of the k closest points to 'test_sample' inside self.X_train
    """

    nn_dist = np.full(self.k, np.inf)
    nn_index = np.full(self.k, -1)

    for index, sample in enumerate(self.X_train):
      dist = l2_dist(sample, test_sample)

      #if distance smaller than largerst k neighbour, replace it.
      if dist < nn_dist[self.k-1]:
        nn_dist[self.k-1] = dist
        nn_index[self.k-1] = index

        top = len(nn_dist)-1
        #sort new k_neighbour into list
        for j in range(len(nn_dist)-1):
          
          if nn_dist[top-j] < nn_dist[top-j-1]:

            temp_dist = nn_dist[top-j]
            temp_index = nn_index[top-j]

            nn_dist[top-j] = nn_dist[top-j-1]
            nn_index[top-j] = nn_index[top-j-1]

            nn_dist[top-j-1] = temp_dist
            nn_index[top-j-1] = temp_index
     
    return nn_index

  def predict(self, X_test):

    """
    Predicts the labels of a sample set

    Param X_test: A numpy array containing a sample set

    Return: The predicted labels as a numpy array
    """

    pred_labels = np.zeros(np.shape(X_test)[0])
    for index, sample in enumerate(X_test):
      nn_index = self.find_k_nearest_neighbours(sample)
      label = self.get_label(nn_index)
      pred_labels[index] = label

    return pred_labels

  def get_k(self):
    
    """
    Return: The value of the attribute k, where k is the number of neighbours considered.
    """

    return self.k

  def find_k(self):

    """
    Finds the optimal value for k.

    Return: The optimal value for k as an integer.
    """

    best_score = np.NINF
    poss_k_vals = [1,2,3,4,5,6,7,8,9,10]
    folds = KFold(n_splits=5, shuffle=True)
    best_k = poss_k_vals[0]

    for k_candidate in poss_k_vals:
      total_score = 0
      for train_index, test_index in folds.split(self.X_train, self.y_train):
        trial_knn = Knn(self.X_train[train_index], self.y_train[train_index], k = k_candidate)
        trial_pred = trial_knn.predict(self.X_train[test_index])
        total_score += r2_score(self.y_train[test_index], trial_pred)
      avg_score = total_score/5
  
      if avg_score > best_score:
        best_score = avg_score
        best_k = k_candidate

    return best_k 
