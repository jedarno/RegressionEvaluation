import numpy as np

def make_square(X):
  r,c  = np.shape(X)

  if r > c:
    pad = ((0, 0), (0, r-c)) 

  elif c > r:
    pad = ((0, c-r), (0,0)) 

  else:
    #X is already square!
    return X

  return np.pad(X, pad, mode="constant", constant_values=0)
