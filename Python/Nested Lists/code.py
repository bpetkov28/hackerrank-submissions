if __name__ == '__main__':
    my_list = []
    score_list = []

    for _ in range(int(input())):
        sub_list = []
        name = input()
        score = float(input())
        sub_list = [name,score]
        score_list.append(score)
        my_list.append(sub_list)
        sub_list = []

    score_list.sort()
    second_lowest = min(score_list)
    for el in score_list:
        if el > min(score_list):
            second_lowest = el
            break

    second_lowest_names = []
    for student_data in my_list:
        if student_data[1] == second_lowest:
            second_lowest_names.append(student_data[0])

    second_lowest_names.sort()

    for eachName in second_lowest_names:
        print(eachName)