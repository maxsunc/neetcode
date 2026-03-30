class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # 0 = treasue
        # -1 = No
        # land

        # find distance to nearest treasure chest for each land place
        # (cant go on water though)
        # call bfs on each point of land

        # instead of going on land and calling bfs on it why dont we start at the treasure chests and find the nearest land points from them
        # use bfs from the treasure point spots

        # at the end do a quick sweep: If any values are inf then make them -1 (isolated land from treasure)
        

        # restsate in own words and askcaobut input constraints


        # iterate to find a treasure chest


        # call bfs on that treasure chest looking for positive values and replace with distance if dist < val
        
        # ignore -1
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def isValid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):

                if grid[i][j] == 0:
                    # we found treasure so lets perform bfs on this

                    q = deque()
                    q.append((i,j,0))
                    seen = set()
                    # print(f"Found a 0 {seen}")
                    while q:
                        # pop off
                        entry = q.popleft()
                        newDist = entry[2] + 1
                        # look in left right up down directions from entry
                        for dir in directions:
                            newRow = dir[0] + entry[0]
                            newCol = dir[1] + entry[1]
                            
                            if (newRow,newCol) in seen:
                                continue
                            
                            # check if the place is valid and  land or not 
                            if isValid(newRow, newCol) and grid[newRow][newCol] != -1:
                                # print(f"Visiting {newRow},{newCol}")
                                seen.add((newRow,newCol))
                                # add it to the queue then for processing since its valid land
                                q.append((newRow,newCol,newDist))
                                # also process it
                                grid[newRow][newCol] = min(grid[newRow][newCol], newDist)

                                # [6,5,4]
                                # [1,-1,3]
                                # [0,1,2]
                                # L L L
                                # L -1 L
                                # t L L
        
                            






