def lonelyinteger(a):
    if len(a) == 1:
        return a[0]
    while len(a) > 1:
        integer = a.pop()
        print(a)
        if integer not in a:
            return integer
        else:
            # Clear second occurance of integer
            a.remove(integer)
    # If last integer - return it
    return a[0]


if __name__ == '__main__':
    the_lone_integer = lonelyinteger([4, 9, 95, 93, 57, 4, 57, 93, 9])
    print(the_lone_integer)
