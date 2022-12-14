import math

# 2 queues (1:26:00)
# 1 queue + 1 dummy node
# 1 queue (Best)



# Space complexity:
# 1. BFS
# * Balanced Tree: O(N/2) -> O(N)
# * Linked List like Tree: O(1)
#
# 2. DFS
# * Balanced Tree: O(H) -> O(logN)
# * Linked List like Tree: O(N)


from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def iteration(self, root):
        result = []

        if root == None:
            return result

        queue = deque([root])

        while queue:
            level = []
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result
    
    def bfs(self, root):

        def recursion(node, level):

            if len(output) <= level:
                output.append([])

            output[level].append(node.val)

            if node.left:
                recursion(node.left, level + 1)
            if node.right:
                recursion(node.right, level + 1)

            return

        output = []
        recursion(root, 0)
        return output

node3 = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)

node3.left = node9
node3.right = node20
node20.left = node15
node20.right = node7

s = Solution()
result = s.recursion(node3)
print(result)