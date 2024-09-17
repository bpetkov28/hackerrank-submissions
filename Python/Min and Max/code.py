import numpy


n, m = map(int, input().split())

arr = numpy.array([list(map(int, input().split())) for _ in range(m)])

min1 = numpy.min(arr, axis=1)

max_min1 = numpy.max(min1)
print(max_min1)