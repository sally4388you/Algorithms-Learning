from collections import deque

# Undirected Graph (Unweighted)
# O(V+E)
class Solution:
    def BFS(self, graph, src):

        dist = [0] * len(graph)
        queue = deque([(src, 0)])
        visited = [False] * len(graph)
        visited[src] = True

        while queue:

            node, level = queue.popleft()
            for n in graph[node]:

                if visited[n] is False:
                    visited[n] = True
                    dist[n] = level + 1
                    queue.append((n, level + 1))

                    # can stop early if necessay
                    # if n == dst:
                    #     return dist[n]

        return dist
  

graph = [[1, 3], [0, 2], [1], [0, 4, 7], [3, 5, 6, 7], [4, 6], [4, 5, 7], [3, 4, 6]]

s = Solution()
result = s.BFS(graph, 0)
print(result)
