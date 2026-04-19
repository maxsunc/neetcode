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
                return -1
            if (i,curVal) in memo:
                return memo[(i,curVal)]
            val = dfs(i-1, curVal)
            # chek if we can take it
            if coins[i] <= curVal:
                # we can take it 
                v = dfs(i, curVal - coins[i])
                if v == -1 and val == -1:
                    val = -1
                elif val == -1:
                    val = v + 1
                elif v == -1:
                    val = val
                else:
                    val = min(val, v + 1)
            memo[(i,curVal)] = val
            return val
        val = dfs(len(coins) - 1, amount)
        return val

        # take or not to take





