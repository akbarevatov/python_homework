import numpy as np
#define the arrays
array_1 = np.array([2, 3, 4, 5])
array_2 = np.array([1, 2, 3, 4])
# create a custom function for power
def custom_function(number, power):
    return number**power
# vectorize the function
vectorized_power = np.vectorize(custom_function)
#print the result
print(f"Results: {vectorized_power(array_1,array_2)}")