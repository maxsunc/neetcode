class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        # O(nlogn) [-3,-1,-1,0,1,2,2,3]
        # O(n)
            # O(n)
        # O(n^2 + nlogn) --> O(n^2)
        nums.sort()
        # iterate the array and do two point
        for i in range(0, len(nums)):
            k, j = i+1, len(nums) - 1
            a = nums[i]
            while j > k:
                if k == i:
                    k += 1
                    continue
                if j == i:
                    j -= 1
                    continue
                curSum = a + nums[k] + nums[j]
                if curSum == 0:
                    # found a solution
                    potential = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(potential)
                    # there could still be more solutions
                    tmp = nums[k]
                    while nums[k] == tmp and j > k:
                        k += 1
                    
                if curSum > 0:
                    j -= 1
                elif curSum < 0:
                    k += 1


        return list(result)
                    
                


