if __name__ == '__main__':
    n = int(input())
    if n >= 2 and n<=10:
        arr = map(int, input().split())

        my_list = []

        for x in arr:
            if x >=-100 and x<=100:
                my_list.append(x)

        second_score = -101

        for x in my_list:
            if x < max(my_list) and x > second_score:
                second_score = x

        print(second_score)