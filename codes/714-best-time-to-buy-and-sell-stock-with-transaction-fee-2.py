class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        prev0, prev1 = 0, -prices[0]
        for i in range(1, n):
            curr0 = max(prev0, prev1 + prices[i] - fee)
            curr1 = max(prev0 - prices[i], prev1)
            prev0, prev1 = curr0, curr1
        return prev0