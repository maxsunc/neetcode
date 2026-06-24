class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # choose a future time to buy the stock

        # left and right pointer
        # or buy and sell index

        buyIndex = 0
        res = 0

        for sellIndex in range(0, len(prices)):
            if prices[sellIndex] < prices[buyIndex]:
                buyIndex = sellIndex
            res = max(res, prices[sellIndex] - prices[buyIndex])
        return res