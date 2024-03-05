def sockMerchant(n, ar):
    socks_found = [ar.pop()]
    n_pairs = 0
    for i in range(1, n):
        sock = ar.pop()
        if sock in socks_found:
            n_pairs += 1
            socks_found.remove(sock)
        else:
            socks_found.append(sock)
    return n_pairs


if __name__ == '__main__':
    assert sockMerchant(7, [1, 2, 1, 2, 1, 2, 3]) == 2, 'Failed to find two socks in 1nes and 2es'

    assert sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]) == 3, 'Failed to find two socks in 10ns and 20s'
