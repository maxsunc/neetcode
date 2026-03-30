class Solution:
    def trap(self, height: List[int]) -> int:
        # array of height

        # height = []

        # keep track of is the maximum values that are occuring

        # [0,2,0,3,1,0,1,2,3,2,1]

        # [0,2,2,3,3,3,3,3,3,3,3]
        # [3,3,3,3,3,3,3,3,3,2,1]
        #       2  2 3 2 = 9
        # 


        # keep track of the maximum heights from left side and right side

        #

        # O(n) time
        # O(n) space
        res = 0
        leftMax = []
        rightMax = []
        curMax = 0
        # build both arrays
        for i in range(0,len(height)):
            curMax = max(curMax, height[i])
            leftMax.append(curMax)
        curMax = 0
        for i in range(len(height)-1, -1,-1):
            curMax = max(curMax, height[i])
            rightMax.insert(0,curMax)
        
        # get whether it has water kept at that point or not:
        for i in range(0, len(height)):
            minHeight = min(leftMax[i],rightMax[i])
            if minHeight > height[i]:
                res += (-height[i] + minHeight)

        return res
