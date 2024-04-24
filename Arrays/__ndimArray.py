import numpy as np

#print how many dimension are in Array

array_a = np.array(45)
array_b = np.array([1,2,3,4,5,6])
array_c = np.array([[1,2,3,4], [5,6,7,8]])
array_d = np.array([[[1,2,3,4], [5,6,7,8]], [[1,2,3,4], [5,6,7,8]]])

print(array_a.ndim)
print(array_b.ndim)
print(array_c.ndim)
print(array_d.ndim)