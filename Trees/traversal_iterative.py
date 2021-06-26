class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def preorderTraversal(self, root):
        stack = [root]
        output = []
        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return output

    def inorderTraversal(self, root):
        stack = []
        node = root
        output = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            output.append(node.val)
            node = node.right
        return output

    def postorderTraversal(self, root):
        stack = []
        output = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                if node.left:
                    node = node.left
                else:
                    node = node.right

            last_node = stack.pop()
            output.append(last_node.val)
            if stack and stack[-1].left == last_node:
                node = stack[-1].right

        return output

    def morrisTraversal(self, root):
        cur = root
        output = []

        while cur:
            if cur.left:
                rightmost = cur.left
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = cur
                tmp, cur.left = cur.left, None
                cur = tmp
            else:
                output.append(cur.val)
                cur = cur.right

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
# inorder [9, 3, 15, 20, 7]
# preorder [3, 9, 20, 15, 7]
# postorder [9, 15, 7, 20, 3]
result = s.preorderTraversal(node3)
print(result)