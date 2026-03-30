class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix problem

        # multiple of everything EXCEPT nums[i]

        # generate forward and backward prefixes

        # create the multiplication

        # the prefixes will work by being a multiple of all past values EXCEPT the current value
        # do this for forward and backward

        fwd = [1] * len(nums)
        for i in range(1, len(nums)):
            prev = i - 1
            fwd[i] = fwd[prev] * nums[prev]
        
        bwd = [1] * len(nums)

        for i in range(len(nums)-2, -1, -1):
            prev = i + 1
            bwd[i] = bwd[prev] * nums[prev]
        print(fwd)
        print(bwd)

        res = [1] * len(nums)

        for i in range(0, len(nums)):
            res[i] = fwd[i] * bwd[i]
        return res