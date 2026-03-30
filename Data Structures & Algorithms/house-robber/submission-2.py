class Solution:
    def rob(self, nums: List[int]) -> int:
        # for each value choose to rob or skip
        # if we choose to rob then the next value is also taken out

        # arr = [2,9,8,3,6]
        # dp() @ len(arr) == 1: return arr[0]
        # or at len(arr) == 0:  return 0

        # return max(dp(currentMony + arr[0], arr[1:]), dp(currentMoney, arr))

        # in our recursive function keep track of the currentMoney

        # instead of passing the array we can pass the index and just use that
        # saved = {}
        # def dfs(i):
        #     if i == len(nums):
        #         return 0
        #     if i == len(nums) - 1:
        #         return nums[i]
            
        #     if i in saved:
        #         return saved[i]
        #     val = max(dfs(i + 1), nums[i] + dfs(i + 2))
        #     print(f"max for the subarray {nums[i:]} is {val}")
        #     saved[i] = val
        #     # recursive case
        #     return val 
        
        # return dfs(0)
        
        # bottom up approach

        # [2,9,8,3,6]
        # size of the array is increasing !
        # 1 : [2]
        # 2 : [9]
        # 3 : max(8 + 2, 9) = 10
        # 4 : max(10, 9 + 3) = 12
        # 
        rob1, rob2 = 0,0 # previous 2 values
        for i in range(0, len(nums)):
            temp = max(rob1 + nums[i], rob2)

            rob1 = rob2
            rob2 = temp
        
        return rob2


