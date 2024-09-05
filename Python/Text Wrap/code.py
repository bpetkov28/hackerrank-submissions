def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width) 
    word_list = wrapper.wrap(text=string)
    result = ""
    for eachElement in word_list:
        result = result + eachElement + "\n"
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)