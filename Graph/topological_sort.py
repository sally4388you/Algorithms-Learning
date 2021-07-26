from collections import deque

class Solution:
    # Topological Sort
    # Kahn's algorithm
    # Similar to BFS
    def Kahn(self, n, edges):
        
        result = []
        indegree = {}
        is_possible = True

        graph = [[] for _ in range(n)]
        for dest, src in edges:
            # the other way
            graph[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1

        lones = deque([k for k in range(n) if k not in indegree]) # Set of all nodes with no incoming edge


        while lones:
            node = lones.popleft()
            result.append(node)
            if node not in graph:
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        lones.append(neighbor)


        return result if len(result) == n else []


    # Topological Sort
    # DFS
    def DFS(self, n, edges):

        visited = {}
        result = []
        graph = [[] for _ in range(n)]
        for dest, src in edges:
            # graph[src].append(dest)
            graph[dest].append(src)


        def dfs(node):
            flag = visited.get(node, 0)

            # 2: permanent
            if flag == 2:
                return True

            # 1: temporary. not a DAG
            if flag == 1:
                return False

            visited[node] = 1

            for i in graph[node]:
                if not dfs(i):
                    return False

            visited[node] = 2
            result.append(node)

            return True

        
        for i in range(len(graph)):
            if not visited.get(i, 0):
                if not dfs(i):
                    return []

        return result

n = 3
edges = [[0,1],[0,2],[1,2]]

n = 4
edges = [[1,0],[2,0],[3,1],[3,2]]

# n = 3
# edges = [[0,2],[2,0],[1,2]]

s = Solution()

result = s.DFS(n, edges)
print(result)

result = s.Kahn(n, edges)
print(result)