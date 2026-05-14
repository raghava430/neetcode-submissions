from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        board = [["."] * n for _ in range(n)]

        cols = set()
        pos_diag = set()  # row + col
        neg_diag = set()  # row - col

        def backtrack(row):
            # If we placed queens in all rows, save the board
            if row == n:
                solution = ["".join(r) for r in board]
                res.append(solution)
                return

            for col in range(n):
                if (
                    col in cols or
                    (row + col) in pos_diag or
                    (row - col) in neg_diag
                ):
                    continue

                # Place queen
                board[row][col] = "Q"
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)

                backtrack(row + 1)

                # Remove queen
                board[row][col] = "."
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)

        backtrack(0)
        return res