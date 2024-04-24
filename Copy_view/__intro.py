"""
The Difference Between Copy and View
The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

"""
import numpy as np

#create array
arr = np.array([0,1,2,3,4,5,6,7,8])
arr2 = arr.copy()

#change the 1st element in arr
arr[0] = 45
arr2[0] = 4

#print both Arrays
print(arr)
print(arr2)