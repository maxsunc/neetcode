class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        # Make a grid of zeros that is 1 row taller and 1 column wider
        self.prefix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        
        # Fill the grid with box sums
        for r in range(ROWS):
            for c in range(COLS):
                # Add current number + top box + left box - overlap
                self.prefix[r + 1][c + 1] = (
                    matrix[r][c] + 
                    self.prefix[r][c + 1] + 
                    self.prefix[r + 1][c] - 
                    self.prefix[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Shift the indexes by 1 because of our extra zeros
        r1, c1 = row1 + 1, col1 + 1
        r2, c2 = row2 + 1, col2 + 1
        
        # Big box - top box - left box + overlap
        return (
            self.prefix[r2][c2] - 
            self.prefix[r1 - 1][c2] - 
            self.prefix[r2][c1 - 1] + 
            self.prefix[r1 - 1][c1 - 1]
        )