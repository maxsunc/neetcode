class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # sorted?
        # [1,5,10]
        coins.sort(reverse=True)

        # brute force
        print(coins)
        # improve the brute force
        seen = {}
        # backtracking
        def dfs(i, curAmount):
        # starting from the highest value 
        # if amouint - coins[i] > 0: do it
        # 
            # print(f"took {curCoins} coins with {curAmount} left at {i}")
            if curAmount == 0:
                return 0

            if i == len(coins) - 1:
                if curAmount % coins[i] == 0:
                    return int(curAmount // coins[i])
                else:
                    return math.inf

            if (i, curAmount) in seen:
                return seen[(i,curAmount)]

            # case 1: Dont take it and move onto the next element
            minVal = dfs(i + 1, curAmount)
            # check if we can take
            if curAmount >= coins[i]:
                minVal = min(minVal, dfs(i, curAmount - coins[i]) + 1)
            seen[(i,curAmount)] = minVal
            return minVal
        res = dfs(0, amount)
        print(res)
        return res if res != math.inf else -1

        # case 2: Take it and recall at this element (only if we're able to take it)

        # recurrence: return min(dfs(i, curAmount - nums[i]), dfs(i+1, curAmount))
        # base case: if i == 0: return curAmount / coins[i] if it can divide evenly
