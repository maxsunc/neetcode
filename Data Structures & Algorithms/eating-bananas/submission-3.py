class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find the max value
        maxVal = 0

        for i, val in enumerate(piles):
            maxVal = max(maxVal, val)

        # perform binary search from 1 to maxValue O(logm)
        l, r = 1, maxVal
        res = maxVal
        # [1,4,3,2] 
        # 2
        while r >= l:
        # for each value simulate whether it would work or not (O(n))
            m = (r + l) // 2
            if self.testRate(piles, m) <= h:
                # we want the min and this is a valid one
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res


    def testRate(self, piles, k):
        res = 0
        # [1,4,3,2], k = 2
        # returns the number of hours used to eat all bananas at k
        for i in range(0, len(piles)):
            # find the number of k's needed to get it to 0 (ceil)
            hours = math.ceil(piles[i] / k) 
            res += hours

        return res

