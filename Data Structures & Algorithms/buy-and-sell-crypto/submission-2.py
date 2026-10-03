class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minbuy = prices[0]
        maxprofit=0
        for i in range(n):
            maxprofit=max(maxprofit, prices[i]-minbuy) # (maxprofit, currentprofit)
            minbuy=min(minbuy, prices[i]) #(previously seen minimum buying price, current price) -> take minimum if current price is lower
        return maxprofit