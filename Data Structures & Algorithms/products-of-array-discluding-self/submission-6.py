class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output[i] is the product of all integers except for nums[i]

        # compute prefix sum
        # for O(N) time and space complexity solution
        pre,suf = [1 ] * len(nums),[1]  * len(nums)
        curProd = 1
        for i,num in enumerate(nums):
            pre[i] = curProd
            curProd *= num
        
        curProd = 1
        for i in range(len(nums) - 1, -1, -1):
            suf[i] = curProd
            curProd *= nums[i]
        # print(pre)
        # print(suf)
        res = []
        for i in range(0, len(nums)):
            res.append(pre[i] * suf[i])
        return res