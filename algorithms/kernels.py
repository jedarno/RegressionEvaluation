import numpy as np

from algorithms.make_square import make_square

from sklearn.metrics.pairwise import rbf_kernel

def kernel_function(m, n, kernel, d=3, r=1):
  """
  A function that takes two matrices and applies them to a kernel.

  Param m,n: matrices as numpy arrays

  param d: optional parameter for the degree of the polynomial kernel, has a default value of 2.

  param r: optional weighting parameter for the polynomial kerenel, has a default value of 1.

  return: Result of teh kernel function as a Numpy array
  """ 

  if kernel  == 'linear':
    return np.matmul(m,n.T)

  elif kernel == 'poly':
    #Adapted from sklearn 
    #https://github.com/scikit-learn/scikit-learn/blob/95119c13a/sklearn/metrics/pairwise.py#L982
    mn = np.matmul(m, n.T)
    n_features = np.shape(m)[1]
    gamma = 1/n_features
    g_mn = mn * gamma
    g_mnr = g_mn + r
    result = g_mnr ** d
    return result

  #Unused code to implement rbf kernel, was not completed
 # elif kernel == 'rbf':
  #  m = make_square(m)
   # n = make_square(n)
   # result = rbf_kernel(m, n)
   # mn = np.matmul(m,n)
   # mn_r, mn_c = np.shape(mn)
    #restult = result[:mn_r, :mn_c]
   # return result

  else:
    print("ERROR: kernel '",kernel,"'not recognised")
    return None


