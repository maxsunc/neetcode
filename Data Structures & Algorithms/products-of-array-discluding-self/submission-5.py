class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        # [1,2,4,6]

        # multiplied by all except self

        # prefix multi array
        # 
        # [1,2,8,48]
        # [48, 24, 6,1]

        pre = []
        suf = [1 for i in range(0, len(nums))]

        curMulti = 1
        # build the arrays
        for i,val in enumerate(nums):
            pre.append(curMulti)
            curMulti *= val
        curMulti = 1
        print(curMulti)

        for i in range(len(nums) - 1, -1, -1):
            suf[i] = curMulti
            curMulti *= nums[i]

        res = []
        print(suf)
        print(pre)

        for i in range(0, len(nums)):
            val = pre[i] * suf[i]
            res.append(val)
        return res
        