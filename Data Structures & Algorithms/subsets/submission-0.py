class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # [1,2,3]
        # []
        # [1], [2], [3]
        # [1,2]

        # to find each of the results, basically each of the values 
        # choice to take or not take into subset

        res = []


        # helper function that creates scenerio
        def takeOrLeave(index, curSubset):
            if index == len(nums):

                # we're done 
                res.append(curSubset.copy())
                return
            
            # case 1 dont include the element at index:
            takeOrLeave(index + 1, curSubset)

            # case 2: include it
            curSubset.append(nums[index])
            
            takeOrLeave(index+1, curSubset)
            curSubset.pop()

        takeOrLeave(0, [])
        return res

