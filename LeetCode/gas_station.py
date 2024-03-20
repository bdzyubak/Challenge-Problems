def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    has_gas = dict()
    valid_index = None
    for i in range(gas):
        has_gas[i] += gas[i]
        has_gas[i] -= cost[i]

    success = [val for val in gas]
    if not any(success):
        return -1

    else:
        return success.index(True)