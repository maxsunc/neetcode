class Solution:
    def jump(self, nums: List[int]) -> int:
        # find the minimium jumps needed to get to the end

        # keep a dp array initially at -1 meaning it cant get to the end
        # if it isnt negative one then that is the number of jumps needed to get to the end
        if len(nums) == 1:
            return 0
        dp = [-1 for i in range(0,len(nums))]
        dp[len(nums) - 1] = 0

        for i in range(len(nums) - 2, -1, -1):
            jumpLength = nums[i]
            # get the min that isn't -1
            minVal = -1
            # print(f"for {nums[i]}: {dp}")
            for j in range(1, jumpLength + 1): # from 1 to jumpLength inclusive
                index = min(j + i, len(dp) - 1)
                if dp[index] == -1:
                    # skip cuz it cant get to the end
                    continue
                minVal = min(minVal, dp[index]) if minVal != -1 else dp[index]
            # update the min number of jumps neeeded to get to the end from here
            if minVal != -1:
                dp[i] = minVal + 1
        print(dp)
        return dp[0]  # assume always a valid answer