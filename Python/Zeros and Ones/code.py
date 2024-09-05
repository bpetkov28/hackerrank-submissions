import numpy

if __name__ == "__main__":
    n = input().replace(' ','')
    input_vals = []
    
    for val in range(len(n)):
         input_vals.append(int(n[val]))
         
    result = tuple(input_vals)

    print(numpy.zeros(result, dtype=numpy.int))
    print(numpy.ones(result, dtype=numpy.int))

