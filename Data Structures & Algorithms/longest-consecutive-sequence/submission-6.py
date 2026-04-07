class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # longest length in my head

        # 
        # [2,20,4,10,3,4,5]

        # [2,3,4,5]

        # O(n) solution?
        # a solution is starting if and only if there is no prev value 
        # exactly one greater

        # [2,3,4,5,10,20]
        # 
        mySet = set(nums)
        res = 0

        # iterate thru array 
        # 2 cases:
        for num in nums:
            if (num-1) in mySet:
                continue
            else:
        # 1: there is a prev value in mySet (num - 1) in set then continue
                length = 1
                curNum = num + 1
                while curNum in mySet:
                    curNum += 1
                    length += 1
                res = max(res,length)
                
        # 2: there is no prev so explorethe whole seq
        return res

