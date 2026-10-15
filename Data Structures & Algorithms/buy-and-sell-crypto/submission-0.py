class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        size = len(prices)
        l, r, maxProfit = 0, 1, 0

        while r < size:
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                if profit > maxProfit:
                    maxProfit = profit
            else:
                # found a cheaper day for left
                l = r
            # advaced r
            r += 1
        
        return maxProfit