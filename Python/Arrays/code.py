import numpy

def arrays(arr):
    reversed_arr = arr[::-1]
    return numpy.array(reversed_arr, float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)