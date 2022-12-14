# Directed Graph (Arbitrarily Weighted)
# O(VE)
#
#
# Bellman-Ford pseudocode
#
# initialize_single_source(G, s)
# for i = 1 to |G.V|-1
#     for each edge (u, v) of G.E
#         relax(u, v, w)
# for each edge (u, v) of G.E
#     if v.d > u.d + w(u, v)
#         return False
# return True
#

from collections import deque

class Solution:
    def BellmanFord(self, graph, src):

        n = len(graph)
        dist = [float("Inf")] * n
        dist[src] = 0

        for _ in range(n - 1):
            # for u, v, w in self.graph:
            #     if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            #             dist[v] = dist[u] + w
            visited = set()
            queue = deque([src])
            while queue:
                u = queue.popleft()
                for v, w in graph[u]:
                    if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        if v not in visited:
                            visited.add(v)
                            queue.append(v)

        # Detect negative cycle
        queue = deque([src])
        visited = set()
        while queue:
            u = queue.popleft()
            visited.add(u)
            for v, w in graph[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
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
result = s.BellmanFord(graph, 0)
print(result)