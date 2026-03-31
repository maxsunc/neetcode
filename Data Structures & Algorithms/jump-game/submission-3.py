import sys
sys.setrecursionlimit(5000)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # maximum jump length is 0?

        # [1,2,0,1,0]
        
        # once we get to the last index we're done!

        # [1,2,1,0,1]
        memo = {}
        # brute force solution: backtracking: Try all possible jumpping patterns
        # save the result of places we jumped into a memo whether it works or not by index
        def dfs(i):
            # print(f"at {i}")
            if i == len(nums) - 1:
                # print("return True!!!")
                return True # we made it
            if nums[i] == 0:
                return False # didnt make it

            if i in memo:
                return memo[i]

            verdict = False
            for jump in range(1, nums[i] + 1):
                index = min(len(nums) - 1, jump + i)
                # from 1 - nums[i ] inclusive try all
                if dfs(index):
                    verdict = True
                    break
            memo[i] = verdict
            return verdict
        return dfs(0)

        # memoization approach


        # DP approach bottom up
        # [1,2,0,1,0]
        # [True, True, False, True, True]
        # if len(nums) == 1:
        #     return True
        # dp = [False for i in range(0, len(nums))]
        # dp [len(nums) - 1] = True



        # for i in range(len(nums) - 2, -1, -1):
        #     maxLength = nums[i]
        #     # go backward and see if we can get to a true
        #     for j in range(1, maxLength + 1):
        #         ind = i + j
        #         if dp[ind]:
        #             # print("foun d a true")
        #             dp[i] = True
        #             break
        # print(dp)
        # return dp[0]




        # greedy approach goes for the best possible result

        # [1,2,1,0,1]
