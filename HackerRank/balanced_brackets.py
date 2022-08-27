# def isBalanced(s):
#     brackets_balanced = 'YES'
#     brackets_balanced = check_balanced(s,brackets_balanced)
#     return brackets_balanced

# def check_balanced(s,brackets_balanced): 
#     if brackets_balanced == 'YES': 
#         for i in range(len(s)-1): 
#             first = s[i]
#             second = s[i+1]
#             print('First: ' + first + ' ' + 'Second: ' + second)
#             if not matched(first,second): 
#                 substring = s[i+1:]
#                 if len(substring)>1: 
#                     brackets_balanced = check_balanced(substring,brackets_balanced)
#                 else: 
#                     brackets_balanced == 'NO'
#     return brackets_balanced

# table =  { ')': '(', ']':'[', '}':'{' }

# def isBalanced(s): 
#     stack = []
#     for x in s:
#         if stack and table.get(x) == stack[-1]:
#             stack.pop()
#         else:
#             stack.append(x)
#     if stack: 
#         return 'NO'
#     else: 
#         return "YES"

def isBalanced(s): 
    stack = []
    for char in s: 
        if stack and matched(stack[-1],char): 
            stack.pop()
        else: 
            stack.append(char)
    print(stack)
            
    if stack: 
        balanced = 'NO'
    else: 
        balanced = 'YES'
    return balanced

def matched(first,second): 
    if first == '{' and second == '}': 
        return True
    elif first == '[' and second == ']': 
        return True
    elif first == '(' and second == ')': 
        return True
    else: 
        return False

# if __name__ == '__main__': 
#     t = int(raw_input().strip())
#     for a0 in xrange(t):
#         expression = raw_input().strip()
#     if is_matched(expression) == True:
#         print "YES"
#     else:
#         print "NO"
    
    # s = '{[()]}' 
    # print('New test case: ' + s)
    # assert isBalanced(s) == 'YES'

    # s = '{[(])}' 
    # print('New test case: ' + s)
    # assert isBalanced(s) == 'NO'

    # s = '{{[[(())]]}}' 
    # print('New test case: ' + s)
    # assert isBalanced(s) == 'YES'

    # s = '(([}[{{[[[})}(][(](]]}[]])()([{(]{(({([}[)(}{)][})[[(}])[]{]){{((((}[{]})])}]{(])]}}}{({)[)][[)[})(][[[}}{][]{[())]}[}{}]((]))((}}([(})[[{[}([[}{(]{})}}]}}}[[{[){[[({}[[](}]{]){}]{[]){[[(}}))}))}])([]}{}{{[}){[({([{)])()[[)((]' 
    # print('New test case: ' + s)
    # assert isBalanced(s) == 'NO'

    # print('Done.')