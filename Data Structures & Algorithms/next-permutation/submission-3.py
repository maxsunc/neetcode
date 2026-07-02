class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # we want to modify nums right?
        # can nums contain duplicate values

        # brute force: generate all permutations of the sorted array
        # really really slow: factorial amount of generations

        # raw thoughts
        # want the lexicographically greater permutation
        # [1,2,3] --> [1,3,2]
        # look for a pivot as the first index

        # nums[pivot + 1] > nums[pivot]:
        # increasing
        # suffix after pivot is decreasing so we need to increase nums[pivot]
        # if no pivot exists then the whole array is decreasing:
        # [3,2,1] --> reverse the array

        # 3. otherwise: find the smallest number to the right that is greater than nums[pivots]

        # swap the two positions
        # then return

        n = len(nums) 
        if n == 1:
            return nums
        # 1. find the pivot
        # pivot is the first index from the right where nums[pivot] < nums[pivot+1]
        pivot = n - 2
        # look for decreasing
        
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1

        # 2. find the successor to swap with the pivot
        # if the pivot is -1 then we go out of bounds
        if pivot >= 0:
            # successor rightmost value with < nums[pivot]
            # suffix is decreasing, the first greater number from the rightmost
            # is the smallest possible number greater than nums[pivot]
            successor = n - 1

            while nums[successor] <= nums[pivot]:
                successor -= 1
            
            # swap pivot with the successor
            nums[pivot],nums[successor] = nums[successor],nums[pivot]

        # 3. reverse the suffix after pivot
        # left and right pointers to reverse
        left = pivot + 1
        right = n - 1
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -=1
        
