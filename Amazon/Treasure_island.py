# https://leetcode.com/discuss/interview-question/347457

from collections import deque

class Solution:
    def minSteps(self, grid):

        q = deque()
        q.append((0, 0))
        grid[0][0] = 'D' # mark as visited
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)];
        steps = 1
        while q:
            for i in range(len(q)):
                p_x, p_y = q.popleft()
            
                for x, y in dirs:
                    r = p_x + x
                    c = p_y + y
                    
                    if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] != 'D' :
                        if grid[r][c] == 'X':
                            return steps
                        grid[r][c] = 'D'
                        q.append((r, c))

            steps += 1
        

        return -1


grid = [
    ['O', 'O', 'O', 'O'],
    ['D', 'O', 'D', 'O'],
    ['O', 'O', 'O', 'O'],
    ['X', 'D', 'D', 'O']
]


s = Solution()
result = s.minSteps(grid)
print(result) # 5

