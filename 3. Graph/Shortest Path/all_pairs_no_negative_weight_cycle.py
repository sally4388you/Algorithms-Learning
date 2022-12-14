# Directed Graph
#
# Johnson's
# # ç(s, v) is the value of shortest path between s and v
# 
# computing G', where G' = G.V U {s}
#     G'E = G.E U {(s, v): v in G.V}, and
#     w(s, v) = 0 for all v in G.E
# if BELLMAN-FORD(G', w, s) == False
#     print 'the input graph contains a negative-weight cycle'
# else
#     for each vertex v in G'V
#         set h(v) to the value of ç(s, v) computed by the Bellman-Ford algorithm
#     for each edge (u, v) in G'E
#         w'(u, v) = w(u, v) + h(u) - h(v)
#     let D = d[u][v] be a new n X n matrix
#     for each vertex u in G'V
#         run DIJKSTRA(G, w', u) to compute ç'(u, v) for all u in G'.V
#         for each vertex v in G'V
#             d[u][v] = ç'(u, v) + h(v) - h(u)
#     return D


import math
import heapq

class Solution:
    def Johnson(self, graph):

        n = len(graph)
        dist = [[math.inf] * n for _ in range(n)]
        nonnegative_weights = [[math.inf] * n for _ in range(n)]

        # adjacency list
        for u in range(n):
            nonnegative_weights[u][u] = 0
            for v, w in graph[u]:
                nonnegative_weights[u][v] = w


        # Weights used to modify the original weights
        h = self.BellmanFord(graph)
        if h == False:
            return 'Graph contains negative weight cycle'


        # Modify the weights to get rid of negative weights
        for i in range(n):
            for j in range(n):
                if nonnegative_weights[i][j] != 0:
                    nonnegative_weights[i][j] = (nonnegative_weights[i][j] + h[i] - h[j])


        # Run Dijkstra for every vertex as source one by one
        for src in range(n):
            dist = self.Dijkstra(nonnegative_weights, dist, src)


        # correct distances
        for u in range(n):
            for v in range(n):
                dist[u][v] += h[v] - h[u]


        return dist


    def BellmanFord(self, graph):
      
        # Add a source s and calculate its min
        # distance from every other node
        G = graph[:]
        n = len(G)
        dist = [math.inf] * (n + 1)
        dist[n] = 0

        new_edges = []
        for i in range(n):
            new_edges.append((i, 0))
        G.append(new_edges)


        for _ in range(n):
            for u in range(len(G)):
                for v, w in G[u]:
                    if dist[u] != math.inf and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w


        for u in range(len(G)):
            for v, w in G[u]:
                if dist[u] != math.inf and dist[u] + w < dist[v]:
                    return False
      
        # Don't send the value for the source added
        return dist[:n]



    def Dijkstra(self, graph, dist, src):

        visited = set()
        dist[src][src] = 0
        for _ in range(len(graph)):
            u = self.minDistance(dist[src], visited)
            visited.add(u)
            for v in range(len(graph)):
                if v not in visited and dist[src][v] > dist[src][u] + graph[u][v]:
                    dist[src][v] = dist[src][u] + graph[u][v]

        return dist


    def minDistance(self, dist, visited):
  
        (minimum, minVertex) = (math.inf, 0)
        for vertex in range(len(dist)):
            if vertex not in visited and minimum > dist[vertex]:
                (minimum, minVertex) = (dist[vertex], vertex)
      
        return minVertex



#(node, w)
graph = [[]] * 6
graph[0] = [(1, 5), (2, 3)]
graph[1] = [(2, 2), (3, 6)]
graph[2] = [(4, 4), (5, 2), (3, 7)]
graph[3] = [(4, -1)]
graph[4] = [(5, -2)]
graph[5] = []


graph = [[]] * 5
graph[0] = [(1, 3), (2, 8), (4, -4)]
graph[1] = [(3, 1), (4, 7)]
graph[2] = [(1, 4)]
graph[3] = [(0, 2), (2, -5)]
graph[4] = [(3, 6)]


# with a negative weight cycle
graph = [[]] * 3
graph[0] = [(1, -1)]
graph[1] = [(2, -2)]
graph[2] = [(0, -1)]


s = Solution()
result = s.Johnson(graph)
print(result)