n, m = map(int, input().split())

for i in range(1, (n//2)+1):
    print(('.|.'*(i*2-1)).center(n*3, '-'))
    
print('WELCOME'.center(n*3, '-'))

for i in range((n//2), 0, -1):
    print(('.|.'*(i*2-1)).center(n*3, '-'))