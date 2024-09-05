def swap_case(s):
    list_s = list(s)
    for ch in range(len(list_s)):
        if list_s[ch].islower():
            list_s[ch] = list_s[ch].upper()
        elif list_s[ch].isupper():
            list_s[ch] = list_s[ch].lower()
    
    new_string = ''.join(list_s) 
            
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)