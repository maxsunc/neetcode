class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Diff: distinct combination of coins that add up to amount
        # Diff: Unlimited coins
        # bottom up apporach

        dp = [[0 for i in range(0,amount + 1)] for j in range(0,len(coins))]

        for i in range(0,len(coins)):
            dp[i][0] = 1 # init to 1 for 0

        # compute bottom up the number of ways to get to some coins
        
        
        for i in range(0, len(coins)):
            for j in range(1,amount+1):
                # 1. Ways to make this amount WITHOUT this current coin
                # (Look at the row above)
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                
                # 2. Ways to make this amount WITH this current coin
                # (Look back in the SAME row)
                coin = coins[i]
                if j - coin >= 0:
                    dp[i][j] += dp[i][j-coin]
        
        return dp[len(coins)-1][amount]



        