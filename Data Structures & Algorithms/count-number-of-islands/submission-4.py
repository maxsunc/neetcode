class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # count the number of islands

        # explore each island fully using dfs or bfs
        # i think bfs makes the most sense
        # islands cannot be diagonally connected 
        # if the one has not yet been seen explore that whole island and increment result

        # 
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        seen = set()
        res = 0
        def isValid(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        # some sort of function to explore 
        def bfsExplore(i,j):
            # explore in all direction of 1 that are unseen
            queue = deque()
            
            queue.append((i,j))
            while queue:
                # mark as seen
                entry = queue.pop()
                seen.add(entry)
                for y,x in directions:
                    newEntry = (entry[0] + y, entry[1] + x)
                    if isValid(newEntry[0],newEntry[1]) and grid[newEntry[0]][newEntry[1]] == '1' and newEntry not in seen:
                        # print(f"exploring: {newEntry} from {entry}")
                        # explore this one too
                        queue.append(newEntry)

        # 1. iterate thru grid
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in seen:
                    print(f"found island @ {i}{j}")
                    bfsExplore(i,j)
                    res += 1
        return res
                    
        # 2. if a 1 is not in seen then explore that island (call bfs on it)
        # increment res
        # 2.5. bfs will make all 1s on that island seen