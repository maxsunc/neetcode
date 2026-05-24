class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas = [1,2,3,2], 
        # cost = [2,2,2,2]
        # [-1,0,1,0]
        if sum(gas) < sum(cost):
            return -1
        # here now we're guarunteed a result

        # the station you start at means you have that much gas at that station
        # so we are able to compute gas[i] - cost[i] as the net 
        # NET: [-1,0,-1,3]
        # runningNet: [-1,-1,-2,1]
        # the startp osiiton must be a net positive
        # we want a O(N) solution

        # but for me I only have a O(N^2) solution

        # greedy approach: keep track of the running sum of the net: whenever a find a positive runningSum then 
        # make that position the reult

        # [1,3,4,-10,9]

        # we can immediantly return -1 if the sum of gas isnt bigger than the sum of cost
        # we can keep track of the total current sum
        # if the total current sum is positive then add it
        # net = [-1,0,-1,3]
        # 
        # keep track of the total when it is positive mark the new position
        # 

        # keep track of the total
        # when its negative reset it ( start a new)
        total = 0
        start = -1
        for i in range(0, len(gas)):
            net = gas[i] - cost[i]
            total += net
            if total < 0:
                total = 0
                start = -1 # resets start
            else:
                if start == -1:
                    # its the first time our total is becoming positive
                    start = i
        
        return start
