def valid_parentheses(string):
    counter = 0 
    for i in string:
        if i == '(':
            counter += 1
        elif i == ')':
            counter -= 1
        if counter == -1:
            return False
    if counter == 0:
        return True
    return False

if __name__ == '__main__':
    valid_parentheses("()()")   