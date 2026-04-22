class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # at each step explore all option of taking any element available
        # [1,2,3]
        # [1]
        # [2]
        # [3]
        # we may retunr the answeri n any order
        res = []
        boolArr = [False for i in range(0,len(nums))]


        def backtrack(curArr):
            if len(curArr) == len(nums):
                res.append(curArr.copy())
                return
            
            # explore branches of possibilities
            for i in range(0, len(nums)):
                if not boolArr[i]:
                    # explore that branch
                    # arrSet.add(nums[i])
                    boolArr[i] = True
                    curArr.append(nums[i])
                    backtrack(curArr)
                    # arrSet.remove(nums[i])
                    boolArr[i] = False
                    curArr.pop()
        
        backtrack([])
        return res



