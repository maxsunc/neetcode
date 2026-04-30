class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # to take or not to take in the subset

        # backtracking problem find all cases of subsets

        # [1,2,3]
        # []
        # 2^n possibilities
        res = []

        # basecase: i == len(nums): add curSubset to result
        # recursive: take or not take: add nums[i] to subset or don't
        # O(2^n)


        def backtrack(i, curSubset):
            if i == len(nums):
                res.append(curSubset.copy())
                return
            
            # take or not take
            curSubset.append(nums[i])
            backtrack(i + 1, curSubset)
            # backtracking step
            curSubset.pop()
            backtrack(i+1, curSubset)
        backtrack(0,[])
        return res