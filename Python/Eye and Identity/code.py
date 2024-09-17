import numpy
numpy.set_printoptions(legacy="1.13")

size = numpy.array(list(map(int, input().split(" "))))

print(numpy.eye(size[0], size[1], k=0))