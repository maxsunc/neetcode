class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort the list so when 
        # each place has the choice to either take or not take (and move forward)
        # each integer is unique in candidates?
        # backtracking problem

        # O(m*2^n) 

        # numbers canb e ued an infinite number of time
        res = []
        # take or not take append to result if the curSum == target
        # if the curSum > target return with nothing
        def backtrack(i,curSum,arr):
            if curSum == target:
                res.append(arr.copy())
                return
            if curSum > target or i >= len(candidates):
                return
            

            # recurrsive case add or dont add
            arr.append(candidates[i])
            backtrack(i,curSum + candidates[i],arr)
            # backtracking step: dont takeit
            arr.pop()
            backtrack(i+1, curSum,arr)
        backtrack(0,0,[])
        return res


        