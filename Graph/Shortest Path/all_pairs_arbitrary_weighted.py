# Directed Graph (Arbitrarily Weighted)
# O(V^3)
#
# Floyd Warshall
#
# n = W.rows
# D[0] = W
# for k = 1 to n
#     let D[k] = d[i][j] be a new n X n matrix
#     for i = 1 to n
#         for j = 1 to n
#             d[i][j] = min(d[i][j], d[i][k] + d[k][j])
# return D[n]


import math

class Solution:
    def FloydWarshall(self, graph):

        n = len(graph)
        dist = [[math.inf] * n for _ in range(n)]

        # adjacency list
        for u in range(n):
            dist[u][u] = 0
            for v, w in graph[u]:
                dist[u][v] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # If vertex k is on the shortest path from
                    # i to j, then update the value of dist[i][j]
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # If distance of any vertex from itself becomes negative, then there is a negative weight cycle.
        for i in range(n):
            if (dist[i][i] < 0):
                return "Graph contains negative weight cycle"
                         
        return dist


# no negative wieght cycle
#(node, w)
graph = [[]] * 6
graph[0] = [(1, 5), (2, 3)]
graph[1] = [(2, 2), (3, 6)]
graph[2] = [(4, 4), (5, 2), (3, 7)]
graph[3] = [(4, -1)]
graph[4] = [(5, -2)]
graph[5] = []


graph = [[]] * 8
graph[0] = [(1, 10), (7, 8)]
graph[1] = [(5, 2)]
graph[2] = [(1, 1), (3, 1)]
graph[3] = [(4, 3)]
graph[4] = [(5, -1)]
graph[5] = [(2, -2)]
graph[6] = [(1, -4), (5, -1)]
graph[7] = [(6, 1)]

# with negative wieght cycle
graph = [[]] * 3
graph[0] = [(1, 1)]
graph[1] = [(2, -2)]
graph[2] = [(0, -1)]


s = Solution()
result = s.FloydWarshall(graph)
print(result)