class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # short: Given an array of coins 
        # we want to find the minimium number of coins that make up 
        # target: each coin has no limit on usage

        # clarifying: can it be negatvie
        # can it be ....

        # find the fewest number o coins needed to make up exact target amount
        # if it's impossible return -1




        # we want ot find the number of min coins needed for a given amount
        # if the amount is 0 then we return 0
        # Try using each coin and find the minimum
        # use mmeoization to bump it to O(S) s is amoun
        # 
        memo = {}

        def minCoins(val):
            if val == 0:
                return 0
            if val in memo:
                return memo[val]
            
            minUsed = float('inf')
            for coin in coins:
                if val - coin >= 0:
                    res = minCoins(val - coin) # test what the minCoins is for each coin taken
                    minUsed = min(minUsed, res + 1)
            memo[val] = minUsed
            return minUsed

        
        result = minCoins(amount)
        return result if result != float('inf') else -1

            