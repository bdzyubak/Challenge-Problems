def prime_up_to(n):
    # Find prime numbers up to value
    primes = []
    for i in range(1, n + 1):
        is_prime = True
        print('')
        print('i is: ' + str(i))
        for j in range(2, i):
            # Don't check division by 1 or self
            print('j is: ' + str(j))
            if i % j == 0:
                print('Flagged on i:' + str(i) + ' and j: ' + str(j))
                is_prime = False
        if is_prime:
            primes.append(i)
    return primes


def prime(n):
    # Find n prime numbers 
    primes = []
    i = 1
    while len(primes) < n:
        is_prime = True
        print('')
        print('i is: ' + str(i))
        for j in range(2, i):
            # Don't check division by 1 or self
            print('j is: ' + str(j))
            if i % j == 0:
                print('Flagged on i:' + str(i) + ' and j: ' + str(j))
                is_prime = False
        if is_prime:
            primes.append(i)
        i += 1
    return primes


if __name__ == '__main__':
    n = 10
    assert prime(n) == [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
