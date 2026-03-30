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
        saved = {}
        def dfs(i):
            if i == len(nums):
                return 0
            if i == len(nums) - 1:
                return nums[i]
            
            if i in saved:
                return saved[i]
            val = max(dfs(i + 1), nums[i] + dfs(i + 2))
            print(f"max for the subarray {nums[i:]} is {val}")
            saved[i] = val
            # recursive case
            return val 
        
        return dfs(0)
        