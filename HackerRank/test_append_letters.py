def append_letters(s,letters,history_local=list()): 
    s += letters
    # Record delete action for undo
    history_local.append((2,len(letters)))
    return s, history_local

history = [(2, 2), (1, 'cdefg')]
s = 'ab'
hist = history.pop()
s = append_letters(s,hist[1])
print(history)
# Expect - [(2,2)] - only the un-popped part of history
# Result - [(2,2),(2,5)] - history is modified by reference even though it is neither returned nor passed to append_letters
