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
            if node.left:
                self.inorder_recursion(node.left)

            self.output.append(node.val)

            if node.right:
                self.inorder_recursion(node.right)

    def preorder_recursion(self, node):
        if node: 
            self.output.append(node.val)

            if node.left:
                self.preorder_recursion(node.left)

            if node.right:
                self.preorder_recursion(node.right)

    def postorder_recursion(self, node):
        if node: 
            if node.left:
                self.postorder_recursion(node.left)

            if node.right:
                self.postorder_recursion(node.right)

            self.output.append(node.val)

root = TreeNode(1)
level1_right = TreeNode(2)
level2_left = TreeNode(3)

root.right = level1_right
level1_right.left = level2_left

s = Solution()
result = s.traversal(root)
print(result)