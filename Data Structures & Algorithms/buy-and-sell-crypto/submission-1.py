class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curProfit = 0

        left = 0

        for right in range(0, len(prices)):
            curProfit = max(curProfit, prices[right]- prices[left])
            if prices[right] <= prices[left]:
                left = right
        return curProfit