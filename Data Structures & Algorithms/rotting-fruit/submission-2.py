class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # is it even possible to rot all oranges
        # m by n grid

        # return the number of time it takes for all oranges to become rotten?

        # how do we determine if we can rot all oranges:
        # all oranges should be guarunteed to be all rotten in n * m minutes
        

        # use bfs: append all the rotten oranges to the bfs queue
        # append (position, minute = 0)
        
        # do our bfs iwth the queue

        # for the elemtn in the queue:
        # check all around for fresh oranges and add entries for those:
        # entry = (positon, minute + 1)
        # also rot that square so it doesnt get added again

        # our result is just the max minute we find
        # O(n * m)

        queue = deque()

        # look for rotten
        m, n = len(grid), len(grid[0])
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 2:
                    entry = ((i,j), 0)
                    queue.append(entry)
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def isValid(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        res = 0
        while queue:
            position,minute = queue.popleft()
            res = max(res,minute)
            # check all directions
            for dir in directions:
                newI,newJ = position[0] + dir[0], position[1] + dir[1]
                if isValid(newI,newJ) and grid[newI][newJ] == 1:
                    grid[newI][newJ] = 2
                    newEntry = ((newI,newJ), minute + 1)
                    queue.append(newEntry)
        # check for any fresh, if there is return -1
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 1:
                    return -1
        return res


