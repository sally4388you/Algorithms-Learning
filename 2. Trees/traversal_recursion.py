class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    output = []

    def traversal(self, root):
        self.output = []
        # self.inorder_recursion(root)
        # self.preorder_recursion(root)
        self.postorder_recursion(root)
        return self.output

    def inorder_recursion(self, node):
        if node: 
            self.inorder_recursion(node.left)

            self.output.append(node.val)

            self.inorder_recursion(node.right)

        return self.output

    def preorder_recursion(self, node):
        if node:
            self.output.append(node.val)

            self.preorder_recursion(node.left)

            self.preorder_recursion(node.right)
        
        return self.output

    def postorder_recursion(self, node):
        if node: 
            self.postorder_recursion(node.left)

            self.postorder_recursion(node.right)

            self.output.append(node.val)

        return self.output

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
# inorder [9, 3, 15, 20, 7]
# preorder [3, 9, 20, 15, 7]
# postorder [9, 15, 7, 20, 3]
result = s.traversal(node3)
print(result)