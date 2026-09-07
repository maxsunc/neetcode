class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # must do this in-place

        # if an element is 0 set its entire row and column to 0s

        # brute force: Create another maxtrix of the same legnth
        
        # O(n + m) space solution: store the rows and columns that end up being 0'd

        # this isn't ideal either


        # constant space soliution????

        # ok lets just implement the O(n + m) solution first

        # is it possible to have an empty array?

        # all numbers right?

        n,m = len(matrix),len(matrix[0])

        rowsZero = [0 for i in range(n)]
        colsZero = [0 for i in range(m)]

        for i in range(0, n):
            for j in range(0,m):
                val = matrix[i][j]
                if val == 0:
                    rowsZero[i] = 1
                    colsZero[j] = 1
        # fill in the grid
        for i,val in enumerate(rowsZero):
            if val == 1:
                # fill in i on the grid with 0s
                for j in range(0, m):
                    matrix[i][j] = 0
        for i,val in enumerate(colsZero):
            if val == 1:
                for j in range(0, n):
                    matrix[j][i] = 0
        


        # i think a constant time solution would have to be recursive in natural

        # whenever we encounter a 0 we can call a dfs algorithm on it: 
        # this dfs alogirthm is called fillZerosDfs we go up down left right from i,j filling with zeros but if we find another zero

        # what if we use a new marker: float('inf') or something, then those are our starting points, wej ust look for those instead, we just using the array as the memory holder

        # we would have to do a 3 pass this way: 1st: set the original zeros to the marker

        # 2nd: fill in the columns and rows of those original zeros to zeros (skip the markers for now)

        # 3rd: go through and reset the markers back to 0s