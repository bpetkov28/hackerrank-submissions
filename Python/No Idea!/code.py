# Enter your code here. Read input from STDIN. Print output to STDOUT
first_line = input().split()
N = int(first_line[0])
M = int(first_line[1])

second_line = list(map(int,input().split()))
third_line = set(map(int,input().split()))
fourth_line = set(map(int,input().split()))

if len(second_line) == N and len(third_line) == M and int(first_line[1]) == M:
  happiness = 0
  for i in range(N):
    if second_line[i] in third_line:
      happiness+=1
    elif second_line[i] in fourth_line:
      happiness-=1
    else:
      happiness=happiness

  print(happiness)
else:
  print("Wrong input")