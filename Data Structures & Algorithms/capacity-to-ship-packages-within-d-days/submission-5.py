class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # [2,4,6,1,3,10]
        # 

        # res = weightCapacity
        # weightCapacity >= max(weights)
        # sum(weights) / weightCapacity >= days
        # [1,2,3,4,5]

        def isValidCapacity(capacity):
            dayCounter = 0
            sumWeights = 0
            # add to sum weights
            # print(" for capacity "  +str(capacity) )
            # once sum weights + weights[i] exceeds capacity then increment days
            # clear sumweight and add weights[i]
            for weight in weights:
                # print( " for day "  +str(dayCounter) + ": " + str(sumWeights))
                if sumWeights + weight >= capacity:
                    dayCounter += 1
                    if sumWeights + weight == capacity:
                        sumWeights = 0
                    else:
                        sumWeights = weight
                else:
                    sumWeights += weight
            if dayCounter > days or (sumWeights != 0 and dayCounter == days):
                # print('falseeeee')
                return False
            return True
        # call binary search on these rresults
        # upper max = sum(weights)

        # upper min = max(weights)
        l,r = max(weights), sum(weights)
        # how low can we go
        lowest = sum(weights)

        while r >= l:
            m = (l+r)//2
            print("L: " + str(l) + " R: " + str(r))
            if isValidCapacity(m):
                r = m - 1
                lowest = m
            else:
                l = m + 1
        return lowest
            
            
        

        # [1,5,4,4,2,3] = 19 
        # 19/5 != 3
