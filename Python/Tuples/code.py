if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    my_list = []
    
    for element in integer_list:
        my_list.append(element)
    
    t = tuple(my_list)
    
    
    print(hash(t))