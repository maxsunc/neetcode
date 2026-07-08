class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # are we guarunteed nums is sorted?
        

        # backtracking
        # build the permutations one position at a time?

        # at each step:
        # try every number that has not be used yet
        # add this to the current permutation
        # recurse 
        # undo the choice so we can try another (backtracking)
        # when the current perm is length n we add a copy of it to the answer
        res = []
        
        path = [] # store the current permutatiuon we gen
        
        # use an array to keep track of the elements used
        used = [False] * len(nums)
        
        # backtracking
        def backtrack():
            # base case: path has all number (len matches the nums)
            if len(path) == len(nums):
                res.append(path.copy())
                return
            

            # recursive cae: try placing each unsued number next
            for i in range(len(nums)):
                # has it the number been used yet
                if used[i]:
                    continue
                
                # explore the case where we use this value
                used[i] = True
                path.append(nums[i])

                # explore further with nums[i] included
                backtrack()

                # undo the choice
                path.pop()
                used[i] = False
            
        backtrack()
        return res













