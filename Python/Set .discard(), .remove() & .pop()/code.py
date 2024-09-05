first_line = int(input())
second_line = set(map(int,input().split()))

if first_line == len(second_line):
    third_line = int(input())
    for each_command in range(third_line):
        command = input().split()
        if command[0] == 'pop':
            second_line.pop()
        elif command[0] == 'remove':
            second_line.remove(int(command[1]))
        elif command[0] == 'discard':
            second_line.discard(int(command[1]))

    print(sum(second_line))