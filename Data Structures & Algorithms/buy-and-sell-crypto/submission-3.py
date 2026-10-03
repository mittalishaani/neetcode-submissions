# using approach from rainwater collection question
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxprofit = 0
        currprofit = 0
        leftmin = [0] * n
        leftmin[0] = prices[0]
        for i in range(1, n):
            leftmin[i] = min(leftmin[i - 1], prices[i])
        for i in range(n):
            currprofit = prices[i] - leftmin[i]
            if currprofit > maxprofit:
                maxprofit = currprofit

        return maxprofit
