from typing import List

class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:

        chars = [str(i) for i in range(1,10)]

        def check_valid(element, i, j):
            nonlocal board
            x, y = (i//3)*3, (j//3)*3
            for index_x in range(x,x+3):
                for index_y in range(y,y+3):
                    if index_x == i and index_y == j:
                        continue
                    if board[index_x][index_y] == element:
                        return False
            for index, character in enumerate(board[i]):
                if index == j:
                    continue
                if character == element:
                    return False
            for index in range(0,9):
                if index == i:
                    continue
                if board[index][j] == element:
                    return False
            return True

        terminated = False

        def dfs(i, j):
            nonlocal board
            nonlocal terminated
            if j == 9:
                if i == 8:
                    terminated = True
                    return
                else:
                    dfs(i+1, 0)
                    return

            if board[i][j] == ".":
                for char in chars:
                    if check_valid(char, i, j):
                        board[i][j] = char
                        dfs(i, j+1)
                        if terminated:
                            return
                board[i][j] = "."
            else:
                dfs(i, j+1)

        dfs(0,0)

solution = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solution.solveSudoku(board)
print(board)