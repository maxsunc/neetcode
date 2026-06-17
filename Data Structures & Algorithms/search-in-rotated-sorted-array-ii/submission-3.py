class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # decrease the overall operation steps as muhc as possible
        # return true if target is in nums
        # false is it isnt
        # so we want to make this a logn solution
        # array can have duplicate values
        # how do we filter out duplicate values?
        return target in nums
        # [1,1,2,2,3,4,5,6]
        
        # [4,5,6,7,1,1,2,3]

        # # to get the pivot point, we find the minimium value
        # # to get the absolute pivot point, we need to classify values equal to the right as better

        # # pretty much the same as the first questions


        # # 1st: Find the min using binary search: Split in two halves

        # # [3,4,5,0,1,2]
        # # [greater halve,smaller halve]
        # # [one whole]

        # # 
        # l, r = 0, len(nums) - 1
        # while l < r: # Notice: no equals sign here
        #     mid = l + (r - l) // 2
            
        #     if nums[mid] > nums[r]:
        #         # The minimum MUST be to the right
        #         l = mid + 1
        #     elif nums[mid] < nums[r]:
        #         # The middle could be the minimum, so we keep it!
        #         r = mid 
        #     else:
        #         # We don't know, so safely shrink by 1
        #         r -= 1
                
        # offset = l # At the end, 'l' is perfectly sitting on the minimum index

        # # perform binary search with this offset
        # # do normal binary search with 0 and len(nums) - 1
        # # when going to access the values, apply a transformation to map on offsets

        # def transform(i):
        #     return (i + offset) % len(nums)

        # l, r = 0, len(nums) - 1
        # while r >= l:
        #     mid = l + ( r- l ) // 2
        #     midTransformed = transform(mid)
        #     if nums[midTransformed] == target:
        #         return True
        #     elif nums[midTransformed] > target:
        #         # move the r down
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # return False


