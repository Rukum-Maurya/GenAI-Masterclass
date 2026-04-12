import numpy as np

# Standard Python Way 
python_list = [10, 20, 30]
# You cannot do python_list * 1.2, it will crash! You have to use a loop.

# The AI / Numpy Way
numpy_array = np.array(python_list)

# Creating a 2d array
numpy_2d_Array = np.array([[10,20],[30,40],[50,60]])

# Vectorization: We multiplying whole 2d array by 1.2  to increase all the elements by 20%
updated_prices_2d_array = numpy_2d_Array * 1.2                        

# Vectorization: We multiply the entire array at once! No loops needed.
updated_prices = numpy_array * 1.2

print(updated_prices)
print(updated_prices_2d_array)
# Output: [12. 24. 36.]
"""
Output: [[12. 22.]
         [36. 48.]
         [60. 72.]]

"""

