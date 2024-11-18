class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        pre1, pre2 = 0, 0
        cur = 0
        for i in range(2, len(cost) + 1):
            cur = min(pre1 + cost[i-2], pre2 + cost[i-1])
            pre1, pre2 = pre2, cur
        return cur

