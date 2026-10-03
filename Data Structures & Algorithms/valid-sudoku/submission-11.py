# bitmask
# uses a 9 bit integer to track an entire row/col/square
# eg. presence of a number in that row -> put that bit in integer to 1 from 0
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                val = int(board[r][c]) - 1  # convert to integer then get bit index
                if (1 << val) & rows[r]:  # bitwise AND for current value and already read row.
                    # only returns non 0 if atleast 1 position has '1' in both 1<<val and rows
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & squares[(r // 3) * 3 + (c // 3)]:
                    return False
                # (r // 3) * 3 + (c // 3) is index within square
                # to add to list if not already found
                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                squares[(r // 3) * 3 + (c // 3)] |= (1 << val)
        return True