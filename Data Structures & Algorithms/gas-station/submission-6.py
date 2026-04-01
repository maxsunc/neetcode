class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        
        # keep a running sum when the running sum is less than 0 that means
        # that starting pos didnt work
        startingPos = 0
        curSum = 0

        for i in range(0, len(gas)):
            cg = gas[i] - cost[i]
            curSum += cg
            if curSum < 0:
                # the startpos didnt work start a new
                curSum = 0
                startingPos = i + 1
        
        return startingPos