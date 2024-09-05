# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
en_subs = set(map(int,input().split()))
b = input()
fr_subs = set(map(int,input().split()))

combined_subs = en_subs.union(fr_subs)
print(len(combined_subs))