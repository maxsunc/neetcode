class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        occur = {}
        for num in nums:
            occur[num] = occur.get(num,0) + 1
        res = []
        for key in occur:
            if occur[key] > len(nums) // 3:
                res.append(key)
        return res