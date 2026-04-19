class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # [1,5,10], amount = 12
        # 

        # reccurence: return min(1 + dfs(i, curVal - coins[i]), dfs(i+1, curVal))
        # base case:
        memo = {}

        coins.sort()
        def dfs(i, curVal):
            if curVal == 0:
                return 0
            if i < 0:
                return math.inf
            if (i,curVal) in memo:
                return memo[(i,curVal)]
            val = dfs(i-1, curVal)
            # chek if we can take it
            if coins[i] <= curVal:
                val = min(val, dfs(i, curVal - coins[i]) + 1)
            memo[(i,curVal)] = val
            return val
        val = dfs(len(coins) - 1, amount)
        return val if val != math.inf else -1

        # take or not to take





