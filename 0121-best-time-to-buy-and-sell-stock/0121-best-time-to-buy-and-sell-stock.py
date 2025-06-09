class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            money_gain = prices[i]-mini
            profit = max(profit,money_gain)
            mini = min(mini,prices[i])
        return profit