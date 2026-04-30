class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # m by n integer matrix
        # return in a sprial order

        # dfs algorithm with priority of directions
        # can only move in one direction
        # [[1,2,3],
        # [4,5,6],
        # [7,8,9]]

        # keep track of the seen elements: 
        # recursive algorithm dfs to search in a spiral
        # first direction: right
        # 2nd: down
        # 3rd: left
        # 4th: up
        n,m = len(matrix),len(matrix[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        res = []
        seen = set()
        def isValid(i,j):
            return 0 <= i < n and 0 <= j < m
        # we can go in that direction if it is a valid coord and wasnt seen before
        def dfs(i,j,pastDir):
            # visit it
            seen.add((i,j))
            res.append(matrix[i][j])
            # try moving in the past dir first 
            newI,newJ = i + pastDir[1], j + pastDir[0]
            if isValid(newI,newJ) and (newI,newJ) not in seen:
                # prioritize the past directions
                dfs(newI,newJ, pastDir)
                return
            # visit the directions in order
            for dir in directions:
                newI,newJ = i + dir[1], j + dir[0]
                if isValid(newI,newJ) and (newI,newJ) not in seen:
                    dfs(newI,newJ,dir)
                    break
        #[[1,2,3,4],
        #[5,6,7,8],
        #[9,10,11,12],
        #[13,14,15,16]]
        dfs(0,0,[0,0])
        return res
