# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
en_subs = set(map(int,input().split()))
b = input()
fr_subs = set(map(int,input().split()))
both_subs = en_subs.intersection(fr_subs)
print(len(both_subs))