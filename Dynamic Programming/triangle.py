class Solution:

    def minimumTotal_bottom_up(self, triangle):

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
        return min(triangle[-1])

    def minimumTotal_top_down(self, triangle):
        # matrix = [[0] * len(triangle) for _ in range(len(triangle[len(triangle) - 1]))]
        matrix = []

        for i in range(0, len(triangle)):
            matrix.append([])
            for j in range(0, len(triangle[i])):
                if i == 0 and j == 0:
                    value = triangle[i][j]
                elif j == 0:
                    value = matrix[i - 1][j] + triangle[i][j]
                elif j < len(matrix[i - 1]):
                    value = min(matrix[i - 1][j], matrix[i - 1][j - 1]) + triangle[i][j]
                else:
                    value = matrix[i - 1][j - 1] + triangle[i][j]

                matrix[i].append(value)

        return min(matrix[len(triangle) - 1])

    def divide_conquer(self, triangle):

        def dfs(x, y, n):
            if x == n - 1:
                return triangle[x][y]

            r1 = dfs(x + 1, y, n)
            r2 = dfs(x + 1, y + 1, n)

            return min(r1, r2) + triangle[x][y]

        size = len(triangle)
        return dfs(0, 0, size)

arr = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
s = Solution()
result = s.minimumTotal_top_down(arr)

print(result)
