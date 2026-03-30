class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        numIslands = 0
        directions = [[0,1],[0,-1],[1,0], [-1,0]]
        # edge cases

        def inRange(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def bfs(row, col):
            visited.add((row, col))
            # guarunteed the value here is 1
            # check if the place is visited
            queue = deque()
            queue.append((row,col))

            while queue:
                # get the first element in the queue
                currentDir = queue.pop()

                # move in left right up down seei f any of them is 1
                # if any is 1 then add then to visited and the queue
                for way in directions:
                    newDir = (currentDir[0] + way[0], currentDir[1] + way[1])
                    # check if its a 1
                    if not inRange(newDir[0], newDir[1]):
                        continue
                    if newDir not in visited and grid[newDir[0]][newDir[1]] == "1":
                        queue.append(newDir)
                    visited.add(newDir)

            return


            
            # traverse the island until no more and mark each as visited

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # grid[i][j]
                # check if its visited
                currentTile = grid[i][j]
                if (i,j) not in visited and currentTile == "1":
                    numIslands += 1
                    # search the island to the end marking each 1 as visited
                    bfs(i,j)
                visited.add((i,j))

        return numIslands

#     ["0","0","0","0","0"],
#     ["0","1","1","1","1"],
#     ["0","1","1","0","0"],
#     ["0","0","0","1","1"]

#     iterate thru the matrix

#       visited = set()
#       


# [[]]
# ["1"]