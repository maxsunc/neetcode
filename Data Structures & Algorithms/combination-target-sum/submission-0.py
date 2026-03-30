class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # use backtracking

         # think of a decision tree
         # each number has a decision to take or not take
         # 0
         # 2 or 0
         # 
        res = []

        def backtrack(index, curSum, curList):
            # base case
            if curSum == target:
                newList = curList.copy()
                res.append(newList)
                return
            if index == len(nums):
                return

            # case 1: Take element at index (only do it if we can support it)
            if target >= curSum + nums[index]:
                curList.append(nums[index])
                backtrack(index, curSum + nums[index], curList)
                curList.pop()
            
            # case 2: dont take and go to next element
            backtrack(index + 1, curSum, curList)
        
        backtrack(0, 0, [])
        return res

