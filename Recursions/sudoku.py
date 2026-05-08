class Solution(object):
    def solveSudoku(self, board):
        # Trackers for: 1. Horizontal, 2. Vertical, 3. Grid
        # These make the isSafe check instant.
        self.rows = [[False] * 10 for _ in range(9)]
        self.cols = [[False] * 10 for _ in range(9)]
        self.boxes = [[False] * 10 for _ in range(9)]
        
        # Pre-fill trackers with the existing numbers on the board
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    digit = int(board[r][c])
                    self.rows[r][digit] = True
                    self.cols[c][digit] = True
                    self.boxes[(r // 3) * 3 + (c // 3)][digit] = True
        
        # Start your recursive solver
        self.ss(board, 0, 0)

    def isSafe(self, row, col, digit):
        # Instant check using your three rules
        if self.rows[row][digit]: return False
        if self.cols[col][digit]: return False
        if self.boxes[(row // 3) * 3 + (col // 3)][digit]: return False
        return True

    def ss(self, board, row, col):
        # Base Case: If we reach the end, we are done
        if row == 9:
            return True
        
        # Your Sidebar Logic: Calculate the next cell
        nextR = row
        nextC = col + 1
        if nextC == 9:
            nextR = row + 1
            nextC = 0
            
        # If the current cell is not empty, jump to the next cell immediately
        # This "Fast-Forwarding" is the secret to passing the time limit!
        if board[row][col] != ".":
            return self.ss(board, nextR, nextC)
        
        # Try digits 1-9
        for digit in range(1, 10):
            if self.isSafe(row, col, digit):
                # Place digit and update trackers
                char_digit = str(digit)
                board[row][col] = char_digit
                self.rows[row][digit] = True
                self.cols[col][digit] = True
                self.boxes[(row // 3) * 3 + (col // 3)][digit] = True
                
                # Recursive call
                if self.ss(board, nextR, nextC):
                    return True
                
                # Backtrack: Undo everything
                board[row][col] = "."
                self.rows[row][digit] = False
                self.cols[col][digit] = False
                self.boxes[(row // 3) * 3 + (col // 3)][digit] = False
                
        return False
    ## this is the problem statement of sudoku solver