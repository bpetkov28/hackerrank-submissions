import numpy

n = list(map(int, input().split(' ')))

n_arr = numpy.array(n, int)

print(numpy.reshape(n_arr, (3, 3)))