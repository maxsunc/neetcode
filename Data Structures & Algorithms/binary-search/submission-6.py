class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # search for a target within an array nums: return -1 if it doesnt exist, or the index if it does
        # clarifying: whatsh te time complx needed
        # first sol brute froce
        # to do this in logn time: 
        # one at the end and another at the start find the mid point: since this array is sorted we can cut off one half of the array
        # if it is too big or too small
        l, r = 0, len(nums) - 1

        while r >= l:
            mid = l + (r - l) // 2 # avoid overflow
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                 l = mid + 1
        return -1 # it don't exist