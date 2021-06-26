from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node):
        if not node:
            return node

        queue = deque([node])
        visited = {}
        visited[node] = Node(node.val)

        while queue:
            n = queue.popleft()

            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                visited[n].neighbors.append(visited[neighbor])

        return visited[node]

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

s = Solution()
result = s.cloneGraph(n1)
print(n1.val)
print(n1.neighbors)