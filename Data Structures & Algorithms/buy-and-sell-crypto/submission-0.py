class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [ 3,2,1,4,5,6,7 ]
        #       i j      
        # two pointer i and j, 0, 1
        # j will iterate
        # if j finds a price less than i then itll say i = j
        result = 0
        i = 0
        for j in range(1,len(prices)):
            if prices[j] < prices[i]:
                i = j
            else:
                # we know prices[j] >= prices[i/]
                diff = prices[j] - prices[i]
                result = max(diff, result)

        return result
