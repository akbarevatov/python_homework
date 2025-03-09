import numpy as np

# define the example array
example_array = np.array([32, 68, 100, 212, 77])

# define function that converts from fahrenheit to celcius
def fahrenheit_to_celcius(F):
    return (F-32)*5/9

# vectorize the function
vectorized_function = np.vectorize(fahrenheit_to_celcius)

# print the result for given example
print(vectorized_function(example_array))