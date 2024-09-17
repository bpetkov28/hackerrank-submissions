import numpy

A, B = [numpy.array(list(map(int,input().split()))) for _ in range(2)]
print(numpy.inner(A, B), numpy.outer(A, B), sep ='\n')
