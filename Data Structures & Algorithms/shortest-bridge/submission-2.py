class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # there are two islands in the grid
        # flip values

        # recursion: Bfs/dfs


        # is it possible they're already connected?
        # guarunteed to have two islands?

        # simple: two islands, we want to connect them, how many fips is needed?


        # 1. identify the two islands
        islands = [set(),set()]
        seen = set()
        def isValid(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid)

        def dfs(i,j,curIsland):
            if not isValid(i,j) or (i,j) in islands[curIsland] or grid[i][j] == 0:
                return
            islands[curIsland].add((i,j))
            seen.add((i,j))
            dfs(i + 1, j, curIsland)
            dfs(i - 1, j, curIsland)
            dfs(i , j + 1, curIsland)
            dfs(i, j - 1, curIsland)
        cur = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1 and not (i,j) in seen:
                    dfs(i,j,cur)
                    cur += 1
        # print(list(islands[0]))
        # print(list(islands[1]))

        # 2. somehow find the distance between them
        # O(N^2): look at each coordinate within island1: and compare each to island2 coordinates and 
        # and find the absolute different between i and j add em together 
        
        
        # O(N): multi source bfs
        dist = [[-1 for i in range(0, len(grid[0]))] for j in range(len(grid))]
        # going in round
        queue = deque()
        for coord in list(islands[0]):
            i,j = coord
            dist[i][j] = 0
            queue.append(((i,j), 0))
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        while queue:
            entry = queue.popleft()
            i,j = entry[0]
            dist[i][j] = entry[1]
            if (i,j) in islands[1]:
                # print((i,j))
                return entry[1] - 1
            
            for dir in directions:
                newI,newJ = i + dir[0], j + dir[1]
                if isValid(newI,newJ) and dist[newI][newJ] == -1:
                    dist[newI][newJ] = entry[1] + 1
                    newEntry = ((newI,newJ), entry[1] + 1)
                    queue.append(newEntry)
        return -1

            



        # use BFS to find the minimium number of steps

        # multi-source bfs to optimize

