class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # given a rectangular island heights 
        # height above sea level at cell coordinate (r,c)

        # water can flip in four directions

        # water can flow from a cell beside it with height equa lor lower\

        # placing water at a coordinate and see if it can reach the atlantic and pacific ocean

        # use dp for this aswelli think we could memo solutions so we dont have repeated work

        # that is a O(n ^ 2 * m ^ 2)
        # that is the brute force solution: do it fro every node

        # to make this faster we could memoize the solution
        # brings it down to O(n * m)

        # but the easier solution: think of it in-reverse
        # if the atlantic can from into a node and the pacific can flow into a node then thats good


        # use extra space to mark whether it can reach the atlantic and pacific 
        # look for greater or equal values, then we can explore it

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        # go with the memoization approach
        # memo = [[[False,False] for i in range(0, len(heights[0]))] for j in range(0, len(heights))]
        pacific = [[False for i in range(0, len(heights[0]))] for j in range(0, len(heights))] 
        atlantic = [[False for i in range(0, len(heights[0]))] for j in range(0, len(heights))] 
        seen = set()

        def isValid(i,j):
            return 0 <= i < len(heights) and 0 <= j < len(heights[0])

        def pacificDfs(i,j):
            # go up and right only, --
            # base case: we're at the pacific if 
            if i == 0 or j == 0:
                pacific[i][j] = True
                return True
            if pacific[i][j]:
                return True
            if (i,j) in seen:
                return False
            # check all directions
            seen.add((i,j))
            # check all directions
            # go in each direction of the pacific as well
            for dir in directions:
                newI,newJ = i + dir[0], j + dir[1]
                # are we able to move to this value and is it a pacific block
                if isValid(newI,newJ) and heights[i][j] >= heights[newI][newJ] and pacificDfs(newI,newJ):
                    pacific[i][j] = True
                    return True
            return False





        def atlanticDfs(i,j):
            # go up and right only, --
            # base case: we're at the pacific if 
            if i == len(heights)-1 or j == len(heights[0]) - 1:
                atlantic[i][j] = True
                return True
            if atlantic[i][j]:
                return True
            if (i,j) in seen:
                return False
            # check all directions
            seen.add((i,j))
            # go in each direction of the pacific as well
            for dir in directions:
                newI,newJ = i + dir[0], j + dir[1]
                # are we able to move to this value and is it a pacific block
                if isValid(newI,newJ) and heights[i][j] >= heights[newI][newJ] and atlanticDfs(newI,newJ):
                    atlantic[i][j] = True
                    return True
            return False
        res = []
        for i in range(0,len(heights)):
            for j in range(0, len(heights[0])):
                if pacificDfs(i,j):
                    seen.clear()
                    if atlanticDfs(i,j):
                        res.append([i,j])
                        seen.clear()
        return res
        