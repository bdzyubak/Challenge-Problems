def plusOne(self, digits: list[int]) -> list[int]:
    if digits[-1] != 9:
        digits[-1] += 1
    else:
        digits[-1] = 0
        if len(digits) > 1:
            digits[:-1] = self.plusOne(digits[:-1])
        else:
            digits.insert(0, 1)
    return digits
