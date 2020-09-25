def validparentheses(chars):
    brackets = {
        '{':'}',
        '[':']',
        '(':')',
    }
    start = 0
    my_stack = []
    while start < len(chars):
        if chars[start] == '(' or chars[start] == '[' or chars[start] == '{':
            my_stack.append(chars[start])
        else:
            if len(my_stack) == 0:
                return False
            else:
                char = my_stack.pop()
                if chars[start] != brackets[char]:
                    return False
        start+=1

    if len(my_stack) == 0:
        return True
    else:
        return False
print(validparentheses("()[]{}"))
