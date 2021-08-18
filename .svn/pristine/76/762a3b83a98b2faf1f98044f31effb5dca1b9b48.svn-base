import unittest
import numpy as np

from kernels import kernel_function

"""
Class to test kernel functions. Each kernel has three tests of example
matrix inputs and checks the correct answer is returned.
"""
class Test_kernels(unittest.TestCase):
  
  def test_polynomial(self):
    

  def test_bad_kernel(self):
    A = []
    k = kernel_function(A, A, 'notakernel')
    self.assertEqual(k, None, "Invalid kernels should return None and print error")

  def test_poly_kernel_not_square(self):
    A = np.array([[1,2],[1,2],[1,2]])
    B = np.array([[1,2],[1,2]])
    k = kernel_function(A,B, 'poly', d=2)
    print("K: ",k)
    array = np.array([[50, 50], [50, 50], [50, 50]])
    print(np.shape(k), np.shape(A))
    self.assertEqual(np.shape(k)[1], np.shape(array)[1], "padding should be removed before return")
    
if __name__ == '__main__':
  unittest.main()


