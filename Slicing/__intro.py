# Slicing allows you to extract a portion of the array.
# Syntax: arr[start_index : end_index : step]
# start_index: The index from where the slicing starts (inclusive).
# end_index: The index up to which slicing is done (exclusive).
# step: The interval between elements to be taken.
import numpy as np

#Now create Array
arr = np.array([1,2,3,4,5,6,7])

#slice from 1 to 5
slide_array = arr[1:5]

#Now print Results
print(slide_array)