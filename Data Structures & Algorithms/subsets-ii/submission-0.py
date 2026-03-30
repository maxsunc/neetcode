class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # find all possible subsets

        # subset = 
        # any order

        # For each have the option to either take or not take the number

        # to deal with duplicates we could the sort the array before hand for "free"
        
        # [1,2,1,1]

        # [], [1], [1,2], [1,1], [1,1]

        # [1,1,1,2]

        # [], [1], [1,1], [1,]

        # process them in waves (like bfs)

        # someho keep track of the already seen subsets 
        # 
        nums.sort()
        reze = []

        def backtrack(index, curSubset):
            print(curSubset)
            # base case at the end of the index just add it
            if index == len(nums):
                reze.append(curSubset.copy())
                return



            # case 1: Take it and look at next
            curSubset.append(nums[index])
            backtrack(index + 1, curSubset)
            curSubset.pop()

            # skip duplicates when dont taking it
            dupl = nums[index]
            newIndex = index + 1
            while len(nums) > newIndex and dupl == nums[newIndex]:
                newIndex += 1
            
            backtrack(newIndex, curSubset)
        backtrack(0,[])
        
        return reze


            # case 2: Don't take it and look at next
