class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def traversal(self, root):

        output = []
        stack = []
        node = root

        while stack or node:

            while node:
                stack.append(node)
                node = node.left

            node = stack[-1]
            node = node.right

            if node is None or node != test:
                node = stack.pop()
                output.append(node.val)
                node = None

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
result = s.traversal(node3)
print(result)
