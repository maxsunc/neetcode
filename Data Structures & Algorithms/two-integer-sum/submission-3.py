class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # assume theres nly one solution
        # assume never invalid inputs?

        # sorting and two point. t: nlogn, s:1
        # bruteforce search: t:n^2,s:1

        # hashset see if different exists: t:n, s:n



        hashSet = {}


        for i in range(0,len(nums)):
            n = nums[i]
            hashSet[n] = i

        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in hashSet and hashSet[diff] != i:
                return [i, hashSet[diff]]
        
        return [0,0]
        
