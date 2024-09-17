import numpy

integers = list(map(int, input().split(" ")))
N = integers[0]
M = integers[1]

first_arr = numpy.array([list(map(int, input().split(" "))) for _ in range(N)])
second_arr = numpy.array([list(map(int, input().split(" "))) for _ in range(N)])

print(numpy.add(first_arr, second_arr))
print(numpy.subtract(first_arr, second_arr))
print(numpy.multiply(first_arr, second_arr))
print(numpy.floor_divide(first_arr, second_arr))
print(numpy.mod(first_arr, second_arr))
print(numpy.power(first_arr, second_arr))