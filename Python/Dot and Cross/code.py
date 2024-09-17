import numpy

n = int(input())

A = [list(map(int, input().split())) for _ in range(n)]

B = [list(map(int, input().split())) for _ in range(n)]

print(numpy.dot(A, B))