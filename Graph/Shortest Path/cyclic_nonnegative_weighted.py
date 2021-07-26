# Directed Graph (Non Negative Weighted >= 0)
# with min priority queue with Fibonacci Heap: O(VlgV + E)
#
# Dijkstra pseudocode
#
# initialize_single_source(G, s)
# S = empty set
# Q = G.V
# while Q != empty
#     u = extract_min(Q)
#     S = S U {u}
#     for each edge (u, v) of G.Adj[u]
#         relax(u, v, w)

import heapq

class Solution:
    def dijkstra(self, graph, src):

        dist = [float("Inf")] * len(graph)
        dist[src] = 0

        queue = []
        heapq.heappush(queue, (src, 0))

        # visited all edges at least once O(E)
        while queue:
            # queue operation O(VlgV)
            u, d = heapq.heappop(queue)
            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(queue, (v, dist[v]))

        return dist


#(node, w)
graph = [[]] * 6
graph[0] = [(1, 5), (2, 3)]
graph[1] = [(2, 2), (3, 6)]
graph[2] = [(4, 4), (5, 2), (3, 7)]
graph[3] = [(4, 1)]
graph[4] = [(5, 2)]
graph[5] = []

# with a cycle
graph = [[]] * 3
graph[0] = [(1, 1)]
graph[1] = [(2, 2)]
graph[2] = [(0, 1)]

s = Solution()
result = s.dijkstra(graph, 1)
print(result)