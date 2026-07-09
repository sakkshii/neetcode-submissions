class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        maxProfit = 0 

        for price in prices:
            if price<minP:
                minP = price 
            else:
                profit = price - minP
                if profit > maxProfit:
                    maxProfit = profit 
        return maxProfit
