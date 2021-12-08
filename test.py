class Solution:
    def numDistinct(self, s, t):
        
        M, N = len(s), len(t)
        
        # Dynamic Programming table
        dp = [[0 for i in range(N + 1)] for j in range(M + 1)] 
        
        # Base case initialization
        for j in range(N + 1):
            dp[M][j] = 0
        
        # Base case initialization
        for i in range(M + 1):
            dp[i][N] = 1

        print(dp)
        
        # Iterate over the strings in reverse so as to
        # satisfy the way we've modeled our recursive solution
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
          
                # Remember, we always need this result
                dp[i][j] = dp[i + 1][j]

                # If the characters match, we add the
                # result of the next recursion call (in this
                # case, the value of a cell in the dp table
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
            
        return dp[0][0]


s = "babgbag"
t = "bag"

solution = Solution()
result = solution.numDistinct(s, t)
print(result)



# class Solution:

#     graph = [[0] * 5 for _ in range(5)]
#     visited = [0] * 5

#     def minTransfers(self, transactions):

#         for x, y, amount in transactions:
#             self.graph[x][y] = amount


#         for i in range(len(self.graph)):
#             if self.visited[i] == 0:
#                 self.dfs(i, [i])
#         print(self.graph)

#         count = 0
#         for i in range(len(self.graph)):
#             for j in range(len(self.graph)):
#                 if self.graph[i][j] != 0:
#                     count += 1

#         return count


#     def dfs(self, node, path):

#         if self.visited[node] == 2:
#             path.pop()
#             self.combineComplete(path, node)
#             return False

#         if self.visited[node] == 1:
#             path.pop()
#             self.combineCycle(path, node)
#             return False

#         self.visited[node] = 1

#         for u in range(len(self.graph)):
#             if self.graph[node][u] > 0:
#                 path.append(u)
#                 if not self.dfs(u, path[:]):
#                     path.pop()

#         self.visited[node] = 2

#         return True

#     def combineComplete(self, path, start):
#         v = path[-1]
#         amount = 0

#         for i in range(len(path) - 2, -1, -1):
#             u = path[i]
#             if u == start:
#                 break

#             amount += self.graph[u][v]
#             self.graph[u][v] = 0
#             v = u

#         self.graph[start][path[-1]] += amount
#         # print(path)
#         # print(self.graph)

#         return

#     def combineCycle(self, path, start):
#         print(path)

#         u = None
#         amount = 0

#         for v in path:
#             if u is not None:
#                 print(u, v, self.graph[u][v])
#                 amount += self.graph[u][v]
#                 self.graph[u][v] = 0
#                 u = v
#             elif v == start:
#                 u = v

#         end = path[-1]
#         self.graph[start][end] += amount
#         print(start, end, amount)


#         # if self.graph[end][start] >= self.graph[start][end]:
#         #     self.graph[end][start] -= self.graph[start][end]
#         #     self.graph[start][end] = 0
#         # else:
#         #     self.graph[start][end] -= self.graph[end][start]
#         #     self.graph[end][start] = 0

#         return


# transactions = [[0,1,10],[2,0,5]]

# transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]

# # transactions = [[0,1,5],[1,2,10],[0,2,5]]

# s = Solution()
# result = s.minTransfers(transactions)
# print(result)



