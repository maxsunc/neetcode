class Solution:
    def trap(self, height: List[int]) -> int:
        # compute maxLEft and maxright arry
        # get the min of each
        # compute min(l,r) - height[i] (make it >= 0 )
        # save them to an array and solve
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        curMax = height[0]

        for i in range(0, len(height)):
            
            curMax = max(curMax, height[i])

            maxLeft[i] = (curMax)
        
        curMax = height[len(height)-1]

        for i in range(len(height)-1, -1, -1):
            curMax = max(curMax, height[i])

            maxRight[i] = (curMax)
        
        result = 0
        for i in range(1, len(height)):
            value = min(maxRight[i], maxLeft[i]) - height[i]
            print("adding " + str(value))
            if value > 0:
                result += value
        return result
        