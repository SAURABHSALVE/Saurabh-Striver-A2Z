class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []

        self.nqueens(board, 0, n, ans)

        final_ans = []

        for solution in ans:
            temp = []
            for row in solution:
                temp.append("".join(row))
            final_ans.append(temp)

        return final_ans

    def isSafe(self, board, row, col, n):

        # check row
        for j in range(n):
            if board[row][j] == 'Q':
                return False

        # check column
        for i in range(n):
            if board[i][col] == 'Q':
                return False

        # left diagonal
        i = row
        j = col

        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # right diagonal
        i = row
        j = col

        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def nqueens(self, board, row, n, ans):

        if row == n:

            temp = []

            for i in range(n):
                temp.append(board[i][:])

            ans.append(temp)

            return

        for j in range(n):

            if self.isSafe(board, row, j, n):

                board[row][j] = 'Q'

                self.nqueens(board, row + 1, n, ans)

                board[row][j] = '.'