class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # find the total number of subarrays that sum up to k

        # backtracking

        # try every single subarray: O (N^2) ? Thats the brute force method

        # prefix sum maybe?

        # [1,2,3]
        # [3,2,1]

        # 

        # keep track of the prefixes of the previous subarrays

        # keep track of the curSum
        # if the curSum - k is in our prefixes then add that amount of subarrays to our result
        # the reason why we do this is because there exist that many subarrays to subtract from our current subarray creating subarrays that have the result of sum k
        # [1,2,2,-2,8]

        prefixes = {}

        prefixes[0] = 1
        res = 0

        curSum = 0

        for i in range(0,len(nums)):
            curSum += nums[i]
            # check if a prefix exists to cut our array down
            prefix = curSum - k

            if prefix in prefixes:
                res += prefixes[prefix]
            
            prefixes[curSum] = prefixes.get(curSum,0) + 1
        
        return res