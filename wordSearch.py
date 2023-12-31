import copy
from typing import Optional, List, Tuple

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        index = 0
        visit = [[False for _ in row] for row in board]
        isExist = False
        def dfs(i: int, j:int):
            nonlocal index, visit, isExist
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return
            if visit[i][j] or board[i][j] != word[index]:
                return
            index += 1
            visit[i][j] = True
            if index == len(word):
                isExist = True
                return
            dfs(i-1, j)
            if isExist:
                return
            dfs(i+1, j)
            if isExist:
                return
            dfs(i, j+1)
            if isExist:
                return
            dfs(i, j-1)
            if isExist:
                return
            visit[i][j] = False
            index -= 1


        for x in range(len(board)):
            for y in range(len(board[0])):
                dfs(x, y)
                if isExist:
                    return True

        return False
