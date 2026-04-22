class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # at each step explore all option of taking any element available
        # [1,2,3]
        # [1]
        # [2]
        # [3]
        # we may retunr the answeri n any order
        res = []


        def backtrack(arrSet, curArr):
            if len(arrSet) == len(nums):
                res.append(curArr.copy())
                return
            
            # explore branches of possibilities
            for i in range(0, len(nums)):
                if nums[i] not in arrSet:
                    # explore that branch
                    # print(f"exploring branch with {nums[i]} length: {len(arrSet)}")
                    arrSet.add(nums[i])
                    curArr.append(nums[i])
                    backtrack(arrSet, curArr)
                    arrSet.remove(nums[i])
                    curArr.pop()
        
        backtrack(set(),[])
        return res



