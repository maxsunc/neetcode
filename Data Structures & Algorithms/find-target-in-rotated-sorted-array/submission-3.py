class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # rotated some amount of times: it was a sorted array

        # we just need to find the pivot

        # do binary search with a pivot
        
        # to find the pivot this is logn)


        # array is split into two groups:

        # [3,4,5,6,1,2]

        l,r = 0, len(nums) - 1
        minIndex = r
        while r >= l:
            mid = l + (r - l) // 2
            # print(nums[mid])
            # print(f"now looking at {nums[l]} and {nums[r]} for {nums[mid]}")
            if nums[mid] <= nums[r]:
                minIndex = mid if nums[mid] < nums[minIndex] else minIndex
                r = mid - 1
            else:
                l = mid + 1
            
            # print(minIndex)
        
        offset = minIndex
        # print(offset)

        # perform binary search to see if it exists
        l,r = 0, len(nums) - 1

        while r >= l:
            mid = l + (r-l) // 2
            midTransformed = (mid + offset) % len(nums)
            if nums[midTransformed] == target:
                return midTransformed
            elif nums[midTransformed] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1