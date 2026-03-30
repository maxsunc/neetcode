class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first create pairs   car at i = (position, speed) 
        pairs = []
        # sort by the pairs
        stack = []

        # create our pairs array
        for i in range(0, len(speed)):
            pairs.append((position[i], speed[i]))
        
        pairs = sorted(pairs, reverse = True)

        # iterate through the pairs
        for pair in pairs:
        # if our stack is not empty, compare with the first elemnet on the stack if merge or not
            if stack:
                topPair = stack[-1]
                t1 = (target - topPair[0]) / topPair[1]
                t2 = (target - pair[0]) / pair[1]
                if t2 > t1:
                    stack.append(pair)
            else:
                stack.append(pair)


        return len(stack)
