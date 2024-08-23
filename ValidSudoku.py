from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(set)
        column = defaultdict(set)
        square = defaultdict(set)
        for r in range (0, 9):
            for c in range (0, 9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in column[c] or board[r][c] in square[r//3, c//3]:
                    return False
                else:
                    rows[r].add(board[r][c])
                    column[c].add(board[r][c])
                    square[r//3, c//3].add(board[r][c])
        return True


test1 = Solution()
test1.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
test2 = Solution()
test2.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])