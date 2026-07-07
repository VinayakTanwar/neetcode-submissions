class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        bestbuy = prices[0]

        for i in range(len(prices) - 1 ):
            i += 1
            if prices[i] > bestbuy:
                maxprofit = max(maxprofit, prices[i] - bestbuy)

            bestbuy = min(bestbuy,prices[i])    

            
        return maxprofit 
        