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
        def dfs(i, curAmount, curCoins):
        # starting from the highest value 
        # if amouint - coins[i] > 0: do it
        # 
            
            if curAmount == 0:
                return curCoins

            if i == len(coins) - 1:
                if curAmount % coins[i] == 0:
                    return int(curCoins + curAmount / coins[i])
                else:
                    return math.inf

            if curAmount in seen:
                return seen[curAmount]
            print(f"took {curCoins} coins with {curAmount} left at {i}")

            # case 1: Dont take it and move onto the next element
            # check if we can take
            minVal = math.inf
            if curAmount >= coins[i]:
                minVal = dfs(i, curAmount - coins[i], curCoins + 1)
            minVal = min(minVal,dfs(i + 1, curAmount, curCoins))
            seen[curAmount] = minVal
            return minVal
        res = dfs(0, amount, 0)
        print(res)
        return res if res != math.inf else -1

        # case 2: Take it and recall at this element (only if we're able to take it)

        # recurrence: return min(dfs(i, curAmount - nums[i]), dfs(i+1, curAmount))
        # base case: if i == 0: return curAmount / coins[i] if it can divide evenly
