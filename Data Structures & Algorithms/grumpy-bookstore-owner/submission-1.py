class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # grumpy[i] is 1 if bookstore is angry during the ith minute
        # 
        # customers[i] = minute customer enters
        # find maximum customers that can be satified throughout theh day
        
        # job is to find the maximum customers satisfied due to our minutes ability

        # fixed sliding window of length minutes
        # find the max sum of a fixed sliding window (only add to the sum if it is 1 on that index)

        total = 0
        for i in range(0, len(grumpy)):
            total += abs(grumpy[i]-1) * customers[i]

        # find the largest sum of 1's then add that to total
        ms = 0
        print(total)

        left = 0
        
        curSum = 0
        minutes = min(minutes, len(grumpy))

        for i in range(0, minutes):
            # sum(grumpy[:minutes] * customers[:minutes])
            curSum += grumpy[i] * customers[i]


        for right in range(minutes, len(customers)):
            ms = max(ms, curSum)
            # 
            curSum += grumpy[right] * customers[right]
            curSum -= grumpy[left] * customers[left]
            left += 1
        ms = max(ms, curSum)
        # add the mostSatified from our ability
        total += ms
        return total
        
