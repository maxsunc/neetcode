class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # more than n / 2 times in the array
        # we an assume the majority element always exists in the array

        # count the occurances with a hashmap. Any value with occurance > n//2 is the majority element
        occ = {}
        n = len(nums)
        for num in nums:
            occ[num] = occ.get(num,0) + 1
        
        # iterate thru the hashmap for an occurance > n // 2
        for key in occ:
            if occ[key] > n // 2:
                return key
        return 0