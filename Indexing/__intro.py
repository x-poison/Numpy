import numpy as np
import time

#create Array
arr = np.array([1,2,3,4,5,6])


def print_with_time(message):
    while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"{current_time} - {message}")
        time.sleep(1)

#Print the first Element => 1
for element in arr:
    print_with_time(element)