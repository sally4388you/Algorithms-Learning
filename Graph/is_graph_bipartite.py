from collections import deque

class Solution:
    # bfs
    def isBipartite_bfs(self, graph):
        color = {}
        for node in range(len(graph)):
            if node in color:
                continue

            queue = deque([node])
            color[node] = 0

            while queue:
                n = queue.popleft()

                for i in graph[n]:

                    if i not in color:
                        color[i] = color[n] ^ 1
                        queue.append(i)

                    elif color[i] == color[n]:
                        return False

        return True

    # dfs
    def isBipartite_dfs(self, graph):

        color = {}
        for node in range(len(graph)):
            if node in color:
                continue

            stack = [node]
            color[node] = 0

            while stack:
                n = stack.pop()

                for i in graph[n]:

                    if i not in color:
                        color[i] = color[n] ^ 1
                        stack.append(i)

                    elif color[i] == color[n]:
                        return False

        return True


# arr = [[1,3], [0,2], [1,3], [0,2]]
# arr = [[1,2,3], [0,2], [0,1,3], [0,2]]
arr = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
s = Solution()
result = s.isBipartite_bfs(arr)
print(result)
