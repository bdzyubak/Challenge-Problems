from operator import itemgetter

s = [[3, 4, 7, 11],
[2, 5, 8, 12],
[1, 6, 9, 10]]

# sorted([(4, 2), (0, 3), (0, 1)])  ==  [(0, 1), (0, 3), (4, 2)]

s = sorted(s, key=itemgetter(1, 2))
print(s)

s = sorted(s, key=itemgetter(1, 2))
print(s)
