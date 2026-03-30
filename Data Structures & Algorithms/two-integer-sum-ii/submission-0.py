class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # i1 != i2
        # i1 < i2 
        # O(1)
        # 1,2,3,4
        # 7
        # sum = 5
        # sum < target
        # i ++
        # sum > target
        


        # 1,2,3,4
        # target = 3
        # sum > target 
        # j--, 4 > 3
        # 1,2,3,5
        # target = 5
        # 6 > 5
        # 4 < 5
        # 5
        i = 0
        j = len(numbers) - 1
        currentSum = numbers[i] + numbers[j]
        while currentSum != target:
            if currentSum > target:
                j -= 1
            elif currentSum < target:
                i += 1
            currentSum = numbers[i] + numbers[j]

        indicies = [i+1, j+1]
        return indicies
            
