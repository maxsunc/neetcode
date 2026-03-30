class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted array

        # find numbers such that they add up to target (theres only one unique solution)

        # converging two pointer 

        l, r = 0, len(numbers) - 1

        # keep a running sum, if the sum is too big reduce the end pointer

        # if its too small increase the start pointer

        curSum = numbers[l] + numbers[r]
        while curSum != target:
            if curSum > target:
                r -= 1
            else:
                l += 1
            curSum = numbers[l] + numbers[r]


        return [l+ 1,r + 1]