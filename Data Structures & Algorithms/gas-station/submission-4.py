class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        curSum = 0
        res = 0

        for i in range(0, len(gas)):
            curSum += gas[i] - cost[i]
            if curSum < 0:
                curSum = 0
                res = i + 1
        return res