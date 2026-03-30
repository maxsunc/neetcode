class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find the maximum profit we can make
        # choose one day to buy neetcoin
        # keep track of the maxProfit
        # update buying index when we encounter a smaller value than current smallest
        left = 0

        maxProfit = 0

        for right in range(0, len(prices)):
            
            # check and see if theres a cheaper version
            if prices[right] < prices[left]:
                left = right

            maxProfit = max(maxProfit, prices[right] - prices[left])

        return maxProfit