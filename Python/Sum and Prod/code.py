import numpy

m,n = map(int, input().split())

arr = numpy.array([list(map(int, input().split())) for _ in range(m)])

sum0 = numpy.sum(arr, 0)

print(numpy.prod(sum0))
