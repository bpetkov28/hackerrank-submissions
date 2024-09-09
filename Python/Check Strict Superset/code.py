setA = set(map(int, input().split()))
n = int(input())

check = True

for element in range(n):
    s = set(map(int, input().split()))
    if not (setA.issuperset(s) and setA != s):
        check = False
        break

print(check)
