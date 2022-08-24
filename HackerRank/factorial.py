import math

def factorial(x): 
    if x ==0: 
        cum_x_fact = 1
    else: 
        cum_x_fact = x*factorial(x-1)

    print(cum_x_fact)
    return cum_x_fact

if __name__ == '__main__': 
    x = 0
    assert factorial(x) == math.factorial(x)

    x = 1
    assert factorial(x) == math.factorial(x)

    x = 2
    assert factorial(x) == math.factorial(x)

    x = 7
    assert factorial(x) == math.factorial(x)
    print('Done')