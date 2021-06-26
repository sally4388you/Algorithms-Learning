import math

class Solution:
    # Topological Sort
    # Kahn's algorithm
    # Similar to BFS
    def topologicalSortKahn(self, graph, src):
        
        result = []
        S = [] # Set of all nodes with no incoming edge

        for i in range(len(graph)):
            if not graph[i]:
                empty.append(i)

        while S:
            node = S.pop()
            result.append(node)
            for edge in graph[node]:
                ;

        return result


    # Topological Sort
    # DFS
    def topologicalSortDFS(self, graph, src):
        
        return result

graph = [[1, 3], [0, 2], [1], [0, 4, 7], [3, 5, 6, 7], [4, 6], [4, 5, 7], [3, 4, 6]]

s = Solution()
result = s.BFS(graph, 0)
print(result)