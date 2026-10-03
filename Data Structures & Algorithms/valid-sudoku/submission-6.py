class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):  # to go through all elements of the board
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]  # in its row
                    or board[r][c] in cols[c]  # in its col
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):  # in its square #() in squares shows that it is a tuple
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
