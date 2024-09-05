if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    i = [x for x in range(0,x+1)]
    j = [y for y in range(0,y+1)]
    k = [z for z in range(0,z+1)]
    result = [i,j,k]
    final_result = [[i,j,k] for i in result[0] for j in result[1] for k in result[2] if i+j+k != n]
    print(final_result)
