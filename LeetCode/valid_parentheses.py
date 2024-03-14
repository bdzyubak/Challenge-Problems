def isValid(s: str) -> bool:
    i = 0
    brackets_list = list()

    for character in s:
        if character in ['(', '{', '[']:
            brackets_list.append(character)
        elif character in [')', '}', ']']:
            if not brackets_list:
                return False
            elif not (
                    (character == ')' and brackets_list[-1] == '(') or (character == ']' and brackets_list[-1] == '[') or (
                    character == '}' and brackets_list[-1] == '{')):
                return False
            else:
                brackets_list.pop()

    if brackets_list:
        return False
    return True