class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # minimal length of sub array such that
        # sum(elements) >= k
        

        # keep track of the min elements

        # when sum(elements) >= k:
        # update minElements if is less than minElement
        # minElements = min(minElements, len(elements))
        # 

        # [2,1,5,1,5,3] k=10

        # dynmic sliding window

        # condition to reduce your window

        # sum(elements) >= k

        left = 0
        curSum = 0
        minElements = 0

        for right in range(0, len(nums)):

            curSum += nums[right]
            
            if curSum >= target:
                if minElements == 0:
                    print("minelements == 0" + (str)(right - left+1))
                    minElements = right - left+1
                minElements = min(minElements, right - left+1)

            while curSum >= target:
                # reduce left
                curSum -= nums[left]
                left += 1
                if curSum >= target:
                    minElements = min(minElements, right - left+1)
            
        return minElements




