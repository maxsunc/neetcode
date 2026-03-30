class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # see if tiles can flow into the border tiles, if they can add them to the set 
        # then lets see if tiles can flow into those

        # this way we only need to call dfs on the outer edges

        # tiles can only flow into us if they're equal or greater than us
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        pacific = set()
        n,m = len(heights), len(heights[0])
        def isValidCoord(i,j):
            return 0 <= i < n and 0 <= j < m
        # all tiles from the left and up border are free entry to the set
        def pacificDfs(i, j):
            pacific.add((i,j))
            ourVal = heights[i][j]
            # explore all direction st node is >= us
            for dir in directions:
                # get a new dir and check not seen before and vlaue greater than or equal to us
                newI = i + dir[0]
                newJ = j + dir[1]
                if not isValidCoord(newI,newJ) or (newI,newJ) in pacific:
                    continue
                # if its a border not yet seen then guarunteed
                if newI == 0 or newJ == 0:
                    pacific.add((newI,newJ))
                    pacificDfs(newI,newJ)
                elif not (newI,newJ) in pacific and heights[newI][newJ] >= ourVal:
                    # explore this node
                    pacific.add((newI,newJ))
                    pacificDfs(newI,newJ)
        atlantic = set()
        def atlanticDfs(i, j):
            atlantic.add((i,j))
            ourVal = heights[i][j]
            # explore all direction st node is >= us
            for dir in directions:
                # get a new dir and check not seen before and vlaue greater than or equal to us
                newI = i + dir[0]
                newJ = j + dir[1]
                if (not isValidCoord(newI,newJ)) or (newI,newJ) in atlantic:
                    continue
                # if its a border not yet seen then guarunteed
                if newI == n-1 or newJ == m-1:
                    atlantic.add((newI,newJ))
                    atlanticDfs(newI,newJ)
                elif heights[newI][newJ] >= ourVal:
                    # explore this node
                    atlantic.add((newI,newJ))
                    atlanticDfs(newI,newJ)
        atlanticDfs(n-1,m-1)
        pacificDfs(0,0)
        print(atlantic)
        print(pacific)
        # get the intersection
        res = []
        for entry in atlantic:
            if entry in pacific:
                newEntry = (entry[0],entry[1])
                res.append(newEntry)
        return res
        


        