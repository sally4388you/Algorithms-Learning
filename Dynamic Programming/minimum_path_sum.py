class Solution:
    def minPathSum_top_down(self, grid):
        if len(grid) <= 0:
            return 0

        # or without matrix
        matrix = [[0] * len(grid[0]) for _ in range(len(grid))]

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if i == 0 and j == 0:
                    matrix[i][j] = grid[i][j]
                elif i == 0:
                    matrix[i][j] = matrix[i][j - 1] + grid[i][j]
                elif j == 0:
                    matrix[i][j] = matrix[i - 1][j] + grid[i][j]
                else:    
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1]) + grid[i][j]

        return matrix[len(grid) - 1][len(grid[0]) - 1]

    def minPathSum_bottom_up(self, grid):
        if len(grid) <= 0:
            return 0

        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[i]) - 1, -1, -1):
                if i == len(grid) - 1 and j == len(grid[i]) - 1:
                    continue
                elif i == len(grid) - 1:
                    grid[i][j] = grid[i][j + 1] + grid[i][j]
                elif j == len(grid[i]) - 1:
                    grid[i][j] = grid[i + 1][j] + grid[i][j]
                else:    
                    grid[i][j] = min(grid[i + 1][j], grid[i][j + 1]) + grid[i][j]

        return grid[0][0]

    def minPathSum(self, grid):
        if len(grid) <= 0:
            return 0

        matrix = [0] * len(grid[0])
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[i]) - 1, -1, -1):
                if i == len(grid) - 1 and j == len(grid[i]) - 1:
                    matrix[j] = grid[i][j]
                elif i == len(grid) - 1:
                    matrix[j] = matrix[j + 1] + grid[i][j]
                elif j == len(grid[i]) - 1:
                    matrix[j] = matrix[j] + grid[i][j]
                else:
                    matrix[j] = min(matrix[j], matrix[j + 1]) + grid[i][j]

        return matrix[0]

arr = [[1,3,1], [1,5,1], [4,2,1]]
arr = [[1,3,1], [1,5,1]]
# arr = [[1,2],[5,6],[1,1]]
s = Solution()
result = s.minPathSum(arr)

print(result)