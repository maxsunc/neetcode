class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0 = empty
        # 1 = resh
        # 2 = rotten fruit

        # # every minute fresh fruit that is horizontal or vertical to rotten fruit becomes rotten
        # bfs problem

        # at the start check for rotten fruits and add them to a queue with (curTime, pos)
        
        # if the curTime exceed len(grid) ^ 2 then its not possible and we return -1

        # keep track of seen values as well

        # for each rotten fruit in the queue, explore around it to make the other fruit rotten 

        # continue doingg the queue stuff until the queue is empty then perform a final check

        n = len(grid)
        m = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        # 1: initialize direction, queue with rottenPositions, seen set, curTime
        res = 0
        rotten = deque()
        seen = set()

        def isValid(i,j):
            return 0 <= i < n and 0 <= j < m

        # append all rotten stuff in 
        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] == 2:
                    rotten.append((0,(i,j)))

        # 2: BFS on the queue until empty to keep rotting nearby stuff
        while rotten:
            entry = rotten.popleft()
            # check each direction for fresh fruits append as rotten if they are with curTime + 1
            for dir in directions:
                i = entry[1][0] + dir[0]
                j = entry[1][1] + dir[1]
                if isValid(i,j) and grid[i][j] == 1:
                    grid[i][j] = 2 # rot it
                    # new rotted fruit
                    res = max(res, entry[0] + 1)
                    newEntry = (entry[0] + 1, (i,j))
                    rotten.append(newEntry)

        # 3: after the queue is empty check whether all fruit is rotten, if it is return the curTime if not return -1
        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j] == 1:
                    return -1
        return res


