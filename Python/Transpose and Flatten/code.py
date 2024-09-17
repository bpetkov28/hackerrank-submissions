import numpy

size = list(map(int, input().split(' ')))
N = size[0]
M = size[1]

input_list = []
for i in range(N):
    input_list.append(list(map(int, input().split(' '))))
        
input_arr = numpy.array(input_list, int)

print(numpy.transpose(input_arr))
print(input_arr.flatten())
