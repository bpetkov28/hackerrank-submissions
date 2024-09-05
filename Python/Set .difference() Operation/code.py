# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
en_subs = set(map(int,input().split()))
b = input()
fr_subs = set(map(int,input().split()))
en_only_subs = en_subs.difference(fr_subs)
print(len(en_only_subs))