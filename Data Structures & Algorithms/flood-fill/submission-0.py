class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # m by n of grid integers
        # image is a grid
        # sr,sc is the position we called our floodfill
        # we want to check all those at sr sc to color
        
        # look for colors sr sc in one direction around us
        colorToChange = image[sr][sc]
        def isValid(r,c):
            return 0 <= r < len(image) and 0 <= c < len(image[0])
        
        def dfs(r,c):
            if not isValid(r,c) or image[r][c] != colorToChange:
                return
            # now we know it is the colorToChange at r,c
            image[r][c] = color
            # check the other directions too
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r,c + 1)
            dfs(r,c-1)
        if color != image[sr][sc]:
            dfs(sr,sc)
        return image