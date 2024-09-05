def count_substring(string, sub_string):
    num_occr=0 
    for i in range(len(string)): 
        if string[i:].startswith(sub_string): 
            num_occr=num_occr+1
    return num_occr

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)