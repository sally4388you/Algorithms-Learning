from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def minDepth(self, root):

        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1
        else:
            left = 1 + self.minDepth(root.left)
            right = 1 + self.minDepth(root.right)

            if root.left and root.right:
                return min(left, right)
            else:
                return max(left, right)

node3 = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)

node3.left = node9
node3.right = node20
node20.left = node15
node20.right = node7

node1 = TreeNode(1)
node2 = TreeNode(2)
node1.left = node2

s = Solution()
result = s.minDepth(node3)
print(result)