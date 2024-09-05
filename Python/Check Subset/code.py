# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    len_a = int(input())
    a = set(map(int, input().split()))
    len_b = int(input())
    b = set(map(int, input().split()))
    
    if len(b.intersection(a))==len_a:
        print(True)
    else:
        print(False)
