from collections import deque

class Solution:
    # Topological Sort O(V+E)
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

        nondependent = deque([k for k in range(n) if k not in indegree]) # Set of all nodes with no incoming edge

        while nondependent:
            node = nondependent.popleft()
            result.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    nondependent.append(neighbor)

        return result[::-1] if len(result) == n else []


    # Topological Sort
    # DFS
    def DFS(self, n, edges):

        # Completed, Partial, Blank
        visited = {}
        result = []
        graph = [[] for _ in range(n)]
        for dest, src in edges:
            # graph[src].append(dest)
            graph[dest].append(src)


        def dfs(node):
            flag = visited.get(node, 0)

            # 2: permanent
            # edges = [(1, 2), (1, 3), (2, 3)]
            if flag == 2:
                return True

            # 1: temporary. not a DAG
            # edges = [(1, 2), (2, 3), (3, 1)]
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
            if not visited.get(i, 0) and not dfs(i):
                return []

        return result[::-1]

n = 3
edges = [[0,1],[0,2],[1,2]]

n = 4
edges = [[1,0],[2,0],[3,1],[3,2]]

# n = 3
# edges = [[0,2],[2,0],[1,2]]

# n = 4
# edges = [[1, 3], [3, 0], [1, 2]]

s = Solution()

result = s.DFS(n, edges)
print(result)

result = s.Kahn(n, edges)
print(result)