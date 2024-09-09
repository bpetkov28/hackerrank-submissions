def minion_game(string):
    kevin_points = 0
    stuart_points = 0
    length = len(string)
    
    for i in range(length):
        if string[i] in 'AEIOUaeiou':
            kevin_points += length - i
        else:
            stuart_points += length - i

    if kevin_points > stuart_points:
        print(f"Kevin {kevin_points}")
    elif stuart_points > kevin_points:
        print(f"Stuart {stuart_points}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)