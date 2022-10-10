string = input()
while string != "End":
    if string != 'SoftUni':
        for char in string:
            if char == string[-1]:
                print(char[-1], end = '')
                print(char)
            else:
                print(char, end = '')
                print(char, end = '')
        string = input()
    else:
        string = input()