class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # track cars by (distance, speed)
        # how do we group the cars together

        # no car can overtake eachother so in other words we should order it by position 

        # to determine if a car will become a fleet with another car  ( merges with that car)
        # if it merges just get rid of the car that caught up to it since they're now the same car
        # we dont need timestamps or any of that bs
        #
        # if the car doesn't collide iwth the current car, take the current car off the stack and say this is done
        # do this until the stack is over

        stack = []
        for i in range(0, len(position)):
            entry = (position[i], speed[i])
            stack.append(entry)
        # stack is ordered by position (futherest away)
        stack.sort()
        print(stack)
        # if the bottom guy can't catch up to us nobody can
        res = 0
        curEntry = stack.pop()
        while stack:
            entry = stack[-1]
            time1 = (target - entry[0]) / entry[1]
            time2 = (target - curEntry[0]) / curEntry[1]
            if time1 <= time2:
                # simply pop from the stack and look at next value since this car caught up to us
                stack.pop()
            else:
                # replace the new current since we didnt catch up we know the fleet remains
                curEntry = stack.pop()
                res += 1
        res += 1

        return res


        
