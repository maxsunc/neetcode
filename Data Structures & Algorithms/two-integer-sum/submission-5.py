class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # find two values that sum up to a target
        s = {}

        for i,num in enumerate(nums):
            s[num] = i
        
        # if the different of target - val exists within s then we found a solution
        # whati if there is no solution? there is guarunteed a solution
        for i,num in enumerate(nums):
            val = target - num
            if val in s:
                if s[val] != i:
                    return [i,s[val]]
        
        return [-1,-1]
            

