import numpy

P = list(map(float, input().split()))
X = int(input())
array = numpy.polyval(P, X)
print(array)