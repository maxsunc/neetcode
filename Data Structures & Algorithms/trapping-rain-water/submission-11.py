class Solution:
    def trap(self, height: List[int]) -> int:
        # find the max area that can be trapped between the bars

        # height[i]
        # track the max heights from each side
        # [0,2,0,3,1,0,1,3,2,1]
        # maxHeight from left: [0,2,2,3,3,3,3,3,3]
        # maxHeight from Right:[3,3,3,3,3,3,3,2,1]

        # BRute force: Foreach index find the max left and max right take the min of them

        # O(N), O(N) Time and space

        # O (N) Time with O(1) space?
        # two pointers? 
        # curMax height

        maxFromLeft = [0 for i in range(0,len(height))]
        maxFromRight = [0 for i in range(0,len(height))]

        curMax = height[0]

        for i in range(0,len(height)):
            curMax = max(curMax,height[i])
            maxFromLeft[i] = curMax
        
        curMax = height[len(height) - 1]
        for i in range(len(height) - 1, -1, -1):
            curMax = max(curMax,height[i])
            maxFromRight[i] = curMax
        res = 0
        # print(maxFromLeft)
        # print(maxFromRight)
        # calculate the result

        for i in range(0, len(height)):
            # get the min height
            minH = min(maxFromLeft[i],maxFromRight[i])
            # minHeight subtracted best curVal only addif greater than 0
            res += max(0, minH - height[i])
        
        return res


            
