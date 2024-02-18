from typing import List


# 这题目是傻逼，把障碍物放入口出口
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
                    continue
                if i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                    continue
                if i == 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1]
                    continue
                if j == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j]
                    continue
                if obstacleGrid[i - 1][j] != -1 and obstacleGrid[i][j-1] != -1:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                elif obstacleGrid[i - 1][j] == -1:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]
        return obstacleGrid[-1][-1]
