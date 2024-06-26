def append_letters(s, letters, history_local=list()):
    s += letters
    # Record delete action for undo
    history_local.append((2, len(letters)))
    return s, history_local


def delete_letters(s, num_letters, history_local=list()):
    num_letters = int(num_letters)
    history_local.append((1, s[-num_letters:]))
    s = s[:(-num_letters)]
    # Record append back action for undo
    return s, history_local


def print_letter(s, index):
    letter = s[int(index) - 1]
    print(letter)
    # Do not record history for prints
    return letter


def undo(s, history):
    hist = history.pop()
    if hist[0] == 1:
        s, _ = append_letters(s, hist[1])
    elif hist[1] == 2:
        s, _ = delete_letters(s, hist[1])
    else:
        print(hist)
        raise (ValueError('Unrecognized action recorded in history.'))
    return s


def editor(s, input, history=list()):
    split_line = input.strip().split(' ')
    action_type = int(input[0])
    if action_type not in [1, 2, 3, 4]:
        raise (ValueError('Unsupported operation.'))
    if action_type == 1:
        value = split_line[1]
        s = append_letters(s, value, history)
    elif action_type == 2:
        value = split_line[1]
        delete_letters(s, int(value), history)
    elif action_type == 3:
        value = split_line[1]
        print(s[int(value) - 1])
        # Don't undo prints
    elif action_type == 4:
        if history:
            (action_type, value) = history.pop()
            if action_type == 1:
                # If original action was append, then delete
                delete_letters(s, len(value))
            else:
                # print('Undo delete action.')
                # print(value)
                append_letters(s, value)


# def editor_wrapper(s,ops,history=list()):
#     for op in ops: 
#         result = editor(s,op,history)
#     return result 

if __name__ == '__main__':
    ## Unit tests
    # Append
    s = 'abcde'
    value = 'fg'
    s, history = append_letters(s, value)
    assert s == 'abcdefg' and history[-1] == (2, len(value))

    # Print
    letter = print_letter(s, '6')
    assert letter == 'f'

    s, history = delete_letters(s, '5', history)
    assert s == 'ab' and history[-1] == (1, 'cdefg')

    history = [(2, 2), (1, 'cdefg')]
    s = 'ab'
    s = undo(s, history)
    print(s)
    print(history)
    assert s == 'abcdefg' and history[-1] == (2, 2)
    print('Done')

    # s = 'abcde'
    # ops = ['1 fg', '3 6', '2 5', '4', '3 7','4','3 4']
    # result = ['f']

    # Execution
    q = int(input().strip())
    s = ''
    history = list()
    for _ in range(q):
        line = input()
        # print('Line: ')
        # print(line)
        editor(s, line, history)
