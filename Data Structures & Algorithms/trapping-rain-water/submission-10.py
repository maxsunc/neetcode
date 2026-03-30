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

        # prefix suffix Soln (1):
        # leftMax = []
        # rightMax = []
        # curMax = 0
        # # build both arrays
        # for i in range(0,len(height)):
        #     curMax = max(curMax, height[i])
        #     leftMax.append(curMax)
        # curMax = 0
        # for i in range(len(height)-1, -1,-1):
        #     curMax = max(curMax, height[i])
        #     rightMax.insert(0,curMax)
        
        # # get whether it has water kept at that point or not:
        # for i in range(0, len(height)):
        #     minHeight = min(leftMax[i],rightMax[i])
        #     if minHeight > height[i]:
        #         res += (-height[i] + minHeight)

        # two pointer solution
        
        # converging again

        # the idea: having two pointer at 0, len(height) - 1

        # having maxLeft and maxRight  we will shift and calculate the area for the bottleneck (lowest value)
        # the idea is the left right when calculating the left isnt needed since the maxRight currently is already greater
        # and maxRight currently will only get bigger as we continue so theres no point in checking maxRight
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]

        while r > l:
            # case 1: maxLeft is the bottle neck
            if maxRight >= maxLeft:

                # calculate the array
                area = maxLeft - height[l]
                res += area
                # shift the left over


                l += 1
                maxLeft = max(maxLeft, height[l])
            else:
                # calculate the array
                area = maxRight - height[r]
                res += area
                # shift the left over


                r -= 1
                maxRight = max(maxRight, height[r])



        return res
