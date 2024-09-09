def print_rangoli(size):
    alphabet = [chr(i) for i in range(97,123)]
    alphabet = alphabet[:size]
    indices = list(range(size))
    indices = indices[:-1] + indices[::-1]

    for i in indices:
        start_index = i + 1
        right_side = alphabet[-start_index:]
        left_side = right_side[::-1]
        row = left_side + right_side[1:]
        width = size*4 - 3
        row = "-".join(row)
        result = row.center(width,"-")
        print(result)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)