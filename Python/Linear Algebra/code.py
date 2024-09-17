import numpy

n = int(input())
list1 = []

for i in range(n):
    list1.append(list(map(float, input().split())))
    
arr = numpy.array(list1)
print(round(numpy.linalg.det(arr), 3))
