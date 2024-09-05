# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
en_subs = set(map(int,input().split()))
b = input()
fr_subs = set(map(int,input().split()))
not_both = en_subs.symmetric_difference(fr_subs)
print(len(not_both))