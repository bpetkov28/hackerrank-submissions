def solve(s):
    full_name = s.split(" ")
    full_name_list = []
    for eachName in full_name:
        full_name_list.append(eachName.capitalize())
    
    result = " ".join(full_name_list)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()