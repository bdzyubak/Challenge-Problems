def minCostClimbingStairs(cost: list[int]) -> int:
    n = len(cost)
    cost_total = [cost[0], cost[1]]
    for i in range(2, len(cost)):
        cost_total.append(min(cost_total[i - 1], cost_total[i - 2]) + cost[i])
    return min(cost_total[n - 1], cost_total[n - 2])
