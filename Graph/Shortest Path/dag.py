import math

class Solution:  
  
    def topologicalSort(self, graph, src):
  
        visited = [False] * len(graph)
        stack =[]

        def topoSort(node):
            visited[node] = True
  
            for n, w in graph[node]:
                if visited[n] is False:
                    topoSort(n)
      
            stack.append(node)
            return
  
        # 1. topological sort
        # not easy to write in interative way. might need two visited array to mark temporary/permanent flag
        topoSort(src)

        # 2. calculate
        dist = [math.inf] * len(graph)
        dist[src] = 0
  
        while stack:
  
            node = stack.pop()
  
            for n, w in graph[node]:
                if dist[n] > dist[node] + w:
                    dist[n] = dist[node] + w
  
        return dist


    def DFS(self, graph, src):
        
        stack = [src]
        dist = [math.inf] * len(graph)
        visited = [False] * len(graph)

        dist[src] = 0
        visited[src] = True # useless but...

        while stack:
            node = stack.pop()
            for n, w in graph[node]:
                if visited[n] is False:
                    visited[n] = True
                    stack.append(n)
                    dist[n] = min(dist[n], dist[node] + w)

                    # can stop early if necessay
                    # if n == dst:
                    #     return dist[dst]
  
        return dist

#(node, w)
graph = [[]] * 6
graph[0] = [(1, 5), (2, 3)]
graph[1] = [(2, 2), (3, 6)]
graph[2] = [(4, 4), (5, 2), (3, 7)]
graph[3] = [(4, -1)]
graph[4] = [(5, -2)]
graph[5] = []


s = Solution()
result = s.topologicalSort(graph, 1)
print(result)
