class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # object: find min time t to swim from top left square (0,0)
        # to bottom (n-1,n-1). 
        # at a time t you can only swim to adjacent square if their elevation is less than or equal to t


        # edge cases: only one cell: answer 0

        # bfs or dfs here

        n = len(grid)
        left, right = 0, max(max(row) for row in grid)

        # help function
        def canSwimInTime(t):
            if grid[0][0] > t: 
                return False

            visited = set()
            q = deque([(0, 0)])
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                x, y = q.popleft()
                if (x, y) == (n - 1, n - 1):
                    return True
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                        if grid[nx][ny] <= t:
                            visited.add((nx, ny))
                            q.append((nx, ny))
            return False

        while left < right:
            mid = (left + right) // 2
            if canSwimInTime(mid):
                right = mid
            else:
                left = mid + 1

        return left