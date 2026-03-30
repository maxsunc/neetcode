class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # matrix BFS/DFS
        # 1st step: iterate through the matrix and find 1 value
        visited = set() # set of tuples
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        result = 0
        def validCoord(coord, matrix):
            return 0 <= coord[0] < len(matrix) and 0 <= coord[1] < len(matrix[0])

        # iterate the matrix
        for row in range(0,len(grid)):
            for i in range(0,len(grid[row])):
                if((row,i) in visited):
                    continue
                visited.add((row,i))
                if grid[row][i] == "1":
                    print(f"found a 1 at {(row,i)}")
                    result += 1
                    # perform the bfs to search for how large the island is:
                    queue = deque() # ()
                    queue.append((row,i))
                    while queue:
                        currentCoord = queue.pop()
                        # move left, right, up, down
                        for direction in directions:
                            coord = (direction[0] + currentCoord[0], direction[1] + currentCoord[1])
                            # check if coord is a valid coordinate
                            if(not validCoord(coord,grid) or coord in visited):
                                continue
                            visited.add(coord)
                            # check if its a 1 then add it to queue
                            if grid[coord[0]][coord[1]] == "1":
                                queue.append(coord)

                    
                else:
                    print('found 0')
        return result
#     ["1","1","0","0","1"],
#     ["1","1","0","0","1"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]