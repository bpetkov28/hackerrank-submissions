import numpy


n, m = map(int, input().split())

array = numpy.array([list(map(float, input().split())) for _ in range(n)])

print(numpy.mean(array, axis=1))
print(numpy.var(array, axis=0))
print(round(numpy.std(array), 11))