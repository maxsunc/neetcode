class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1,0,1,2,-1,-4]
        # [-4, -1, -1, 0, 1, 2]
        res = set()
        nums.sort()
        # [-4,1,2,2,3]
        # iterate through the array
        for i in range(len(nums)-2):

            
        # set iteration value to target
            target = -nums[i]


        # see if we can add up to -target
            l,r = i + 1, len(nums)-1
        # if we can, add to result!
            while r > l:
                print("comparing " + str((nums[i], nums[l], nums[r])))
                currSum = nums[l] + nums[r]
                if currSum > target:
                    r -= 1
                elif currSum < target:
                    l += 1
                else:
                    print(" added " + str([nums[i], nums[l], nums[r]]))
                    triplet = (nums[i], nums[l], nums[r])
                    res.add(triplet)
                    l += 1
                    r -= 1
        return list(res)
                    
                


