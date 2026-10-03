#brute force
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9): #for all rows
            seen = set()
            for i in range(9): # to go through each element in row
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen: #check for membership of that number in that row's set
                    return False
                seen.add(board[row][i])
        
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
        
        for square in range(9): #for each 3x3 block
            seen = set()
            for i in range(3): #to get box's row (0,1,2)
                for j in range(3): #to get box's col (0,1,2)
                    row = (square // 3)*3 + i #actual row in board
                    col = (square % 3)*3 + j #actual col in board
                    if board[row][col] ==".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True



