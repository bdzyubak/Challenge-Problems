def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])
    l = 0
    r = rows * cols - 1

    while l <= r:
        mid = (l + r) // 2
        mid_value = matrix[mid // cols][mid % cols]

        if mid_value == target:
            return True
        elif mid_value < target:
            l = mid + 1
        else:
            r = mid - 1

    return False
