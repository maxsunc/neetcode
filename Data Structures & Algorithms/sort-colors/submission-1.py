class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bucket sort / hashmap
        myDict = [0,0,0]

        for i in nums:
            myDict[i] += 1

        result = []

        for i in range(0,len(myDict)):
            for j in range(0, myDict[i]):
                print("adding " + str(i))
                result.append(i)

        for i in range(0, len(result)):
            nums[i] = result[i]

        