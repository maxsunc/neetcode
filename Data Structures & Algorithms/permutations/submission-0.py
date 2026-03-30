class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # find 1,2,3 --> [[1,2,3],[1,3,2],[2,1,3]]

        # how to generate all permuatations:
        # Brute Force: 
        # [[1,2,3],[2,1,3],[]]

        # have a temp list
        temp = []  

        res = []


        # have a boolean array of size n (tru = explored, false otherwise)
        boolArr = [False] * len(nums)
        # iterate thru the array recursively
        def backtrack():
            if temp and len(temp) == len(nums):
                # add it to res and exit
                res.append(temp.copy())
                return
            # pick elements that have not yet been chosen previously 
            for i in range(0, len(boolArr)):
                
                if not boolArr[i]:
                    # haven't added this yet lets explore this branch!
                    boolArr[i] = True
                    temp.append(nums[i])
                    backtrack()
                    temp.pop()
                    boolArr[i] = False # reset 
        
        backtrack()
        return res

        # terminate the recursive path when the whole boolean array is over or (easier) when tmp array is the same length as nums


