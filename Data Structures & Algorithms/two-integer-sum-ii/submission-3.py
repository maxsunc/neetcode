class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted array
        # just use two pointers start and end . Decrease end if sum is too big
        # increase start if sum is too small

        start,end = 0, len(numbers) - 1

        summed = numbers[start] + numbers[end]
        while summed != target:
            if summed > target:
                end -= 1
            elif summed < target:
                start += 1
            summed = numbers[start] + numbers[end]
        
        return [start + 1, end + 1]