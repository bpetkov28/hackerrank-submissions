if __name__ == '__main__':

    s = input()
    def find_type(method_name):
        if any(getattr(char, method_name)() for char in s):
            return True
        return False

    print(find_type('isalnum'))
    print(find_type('isalpha'))
    print(find_type('isdigit'))
    print(find_type('islower'))
    print(find_type('isupper'))