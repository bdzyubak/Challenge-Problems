def hammingWeight(n: int) -> int:
    n = bin(n)[2:]
    num_ones = 0
    for i in n:
        if i == "1":
            num_ones += 1
    return num_ones