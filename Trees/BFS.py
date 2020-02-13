import math

# 2 queues (1:26:00)
# 1 queue + 1 dummy node
# 1 queue (Best)

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

        while len(queue) > 0:
            level = []
            size = len(queue)
            for i in range(0, size):
                head = queue.popleft()
                level.append(head.val)

                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)

            result.append(level)

        return result

    def recursion(self, root):
        output = []
        self.bfs(root, 0, output)
        return output
    
    def bfs(self, node, level, output):
        if not node:
            return
        
        if len(output) < level + 1:
            output.append([])
            
        output[level].append(node.val)
            
        if node.left:
            self.bfs(node.left, level + 1, output)
        if node.right:
            self.bfs(node.right, level + 1, output)

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