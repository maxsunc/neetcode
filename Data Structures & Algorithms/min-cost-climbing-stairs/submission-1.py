class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost contains the cost of taking step from the ith floor of a staircase
        # we want to reach the nth stair ( place after the last step)
        
        # calculate the min cost for each stair
        # base case: minCost(0) = cost[0]
        # minCost(1) = cost[1]

        # reccurence: minCost(n) = min(minCost(n-1) + minCost(n-2)) + COST[I]
        # n = len(cost)
        # minCost = [0 for i in range(0,n + 1)] # since we want to calculate the cost of going to nth stair
        # minCost[0] = cost[0]
        # minCost[1] = cost[1]
        # cost.append(0)

        # for i in range(2, len(minCost)):
        #     minCost[i] = min(minCost[i - 1], minCost[i-2]) + cost[i]
        
        # return minCost[n]

        # recursion with memoization solution
        n = len(cost)
        cost.append(0)
        memo = [0 for i in range(0,n+1)]
        def dfs(val):
            if val <= 1:
                return cost[val]
            if memo[val] != 0:
                return memo[val]
            minC = min(dfs(val-1), dfs(val-2)) + cost[val]
            memo[val] = minC
            return minC
        
        return dfs(n)


        
         