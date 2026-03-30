class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # res = 0
        
        # for start in range(0, len(nums)):
        #     curSum = 0
        #     for i in range(start, len(nums)):
        #         curSum += nums[i]
        #         if curSum == k:
        #             res += 1
        # return res


        # actual solution ngl I have no clue how this works


        prefixs = {}

        prefixs[0] = 1 # empty

        res = 0

        curSum = 0
        for i in range(0, len(nums)):
            # add t ocurSum
            curSum += nums[i]


            res += prefixs.get(curSum - k, 0) 
            # add the sum as an entry to prefixes
            prefixs[curSum] = prefixs.get(curSum, 0) + 1
        return res


                