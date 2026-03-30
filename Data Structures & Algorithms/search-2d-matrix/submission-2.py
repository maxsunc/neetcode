class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # they''re all sorted

        # so we just need to do binary search 2 times

        # vertical binary search to find which row it resides
        # horizontal on that row to actaully find the value

        # determine the row to look at 
        l, r = 0, len(matrix) - 1

        # [mid][0]
        # looking for lower
        m = 0
        while r >= l:
            m = (l + r) // 2
            print(m)
            #[1,10,23]
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1
        row = m if matrix[m][0] < target else m - 1
        if row < 0:
            return False
        print(f"{row} row found")


        # perform binary search on this row
        l, r = 0, len(matrix[row]) - 1
        m = 0
        while r >= l:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False
            


            
        