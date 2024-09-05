# Enter your code here. Read input from STDIN. Print output to STDOUT
len_A = int(input())
A = set(map(int, input().split()))

if len_A == len(A):
    N = int(input())
    
    for eachCommand in range(N):
        
        command, len_subset = input().split()
        input_set = set(map(int, input().split()))
        
        if int(len_subset) == len(input_set):
            if command == 'intersection_update':
                A.intersection_update(input_set)
            elif command == 'update':
                A.update(input_set)
            elif command == 'symmetric_difference_update':
                A.symmetric_difference_update(input_set)
            elif command == 'difference_update':
                A.difference_update(input_set)
            else:
                raise ValueError
    print(sum(A))