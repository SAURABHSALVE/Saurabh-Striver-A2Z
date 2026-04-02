class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # We use dictionaries where the values are SETS 
        # (Sets are great here because they only store unique items)
        cols = {}   # Key: col index, Value: set of numbers seen
        rows = {}   # Key: row index, Value: set of numbers seen
        squares = {} # Key: (r//3, c//3), Value: set of numbers seen

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                
                # Identify which 3x3 square we are in
                # Dividing by 3 tells us the 'coordinate' of the square (0, 1, or 2)
                square_key = (r // 3, c // 3)

                # Initialize the sets if they don't exist yet (your style!)
                if r not in rows: rows[r] = set()
                if c not in cols: cols[c] = set()
                if square_key not in squares: squares[square_key] = set()

                # Check if the number already exists in this row, col, or square
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[square_key]):
                    return False
                
                # If it's new, add it to our trackers
                rows[r].add(val)
                cols[c].add(val)
                squares[square_key].add(val)
                
        return True
## examples 
solution = Solution()
print(solution.isValidSudoku(
    [["5","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]]
))  # Output: True  