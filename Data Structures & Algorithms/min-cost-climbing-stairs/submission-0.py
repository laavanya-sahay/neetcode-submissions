class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        i = 2

        while i < n:
            cost[i] += min(cost[i-1], cost[i-2])
            i += 1

        return min(cost[n-1], cost[n-2])