class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # price[i] = price at day ith

        # [10,]

        # dynamic sliding window iterating thru the prices
        # when we find something smaller than us replace the buy position

        res = 0

        buy = 0

        for i in range(0,len(prices)):
            res = max(res, prices[i] - prices[buy])
            if prices[buy] > prices[i]:
                buy = i
        return res