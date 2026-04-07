class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Diff: distinct combination of coins that add up to amount
        # Diff: Unlimited coins

        # backtracking: Try every single 
        memo = [[-1 for i in range(0, amount+1)] for j in range(0,len(coins))]
        coins.sort()
        # either take or stop taking 

        def dfs(i, curSum):
            # base case
            if curSum >= amount:
                return 1 if curSum == amount else 0
            if i >= len(coins):
                return 0
            
            if memo[i][curSum] != -1:
                return memo[i][curSum]
            
            # take or move onto next
            val = dfs(i, curSum + coins[i]) + dfs(i+1,curSum) # ways to get tto the result both ways here

            memo[i][curSum] = val
            return val
        
        return dfs(0,0)



