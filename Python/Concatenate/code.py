import numpy

metrics = list(map(int, input().split(" ")))
N = metrics[0]
M = metrics[1]
P = metrics[2]

first_arr = numpy.array([list(map(int, input().split(" "))) for _ in range(N)])
second_arr = numpy.array([list(map(int, input().split(" "))) for _ in range(M)])

third_arr = numpy.concatenate((first_arr, second_arr), axis=0)
print(third_arr)