class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # cooldown period of one day

        # [1,3,4,0,4]
        # there is a one day cooldown

        # keep track fo the buy index and the sell index

        # when prices[sell] > prices[buy] then we are able to sell. we can choose to sell and skip one index looking for the next buy index
        # return max()
        # or choose to skip and wait for the next

        # else prices[sell] <= prices[buy]:
        # then set buy = sell since we wont gain anything from selling right now 
        # dp = [[-1 for i in range(0,len(prices))] for j in range(0,len(prices))]
        # def dfs(buy,sell):
        #     if sell >= len(prices):
        #         return 0

        #     if dp[buy][sell] != -1:
        #         return dp[buy][sell]            
        #     val = 0
        #     if prices[sell] > prices[buy]:
        #         # we have the abilitiy to sell if we want
        #         # print(f"{prices[sell]} {prices[buy]}")
        #         val = max((prices[sell] - prices[buy] ) + dfs(sell + 2, sell + 3), dfs(buy, sell + 1))
        #     else:
        #         # print(f"{prices[sell]} less than {prices[buy]}")
        #         # we can't sell since buy is greater than us
        #         buy = sell # found a new min
        #         val = dfs(buy, sell + 1)
        #     dp[buy][sell] = val
        #     return val

        # return dfs(0,0)

        dp = {}

        # O(n) solution each node has decision to buy/sell or cd
        def dfs(i, buying): # i = current index
            if i >= len(prices):
                return 0
            
            if (i,buying) in dp:
                return dp[(i,buying)]

            # we have a choice to either buy or cd if buying
            val = 0
            if buying:
                # print(f"buying at {prices[i]}")
                val = max(dfs(i + 1, False) - prices[i], dfs(i+1, True))
            else:
                # print(f"selling at {prices[i]}")
                val = max(dfs(i + 2, True) + prices[i], dfs(i+1, False))
            dp[(i,buying)] = val
            # print(f"big val: {val}")
            return val

        return dfs(0,True)

        # [1,4,3,0,4]