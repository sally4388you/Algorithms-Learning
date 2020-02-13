class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def inorderTraversal(self, root):
        stack = []
        node = root
        output = []
        while (len(stack) > 0 or node):
            while (node):
                stack.append(node)
                node = node.left
            node = stack.pop()
            output.append(node.val)
            node = node.right
        return output

    def preorderTraversal(self, root):
        stack = [root]
        output = []
        while (len(stack) > 0):
            node = stack.pop()
            if node:
                output.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return output

    def morrisTraversal(self, root):
        output = []
        current = root
        while current:
            if current.left:
                rightmost = current.left
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = current
                tmp = current.left
                current.left = None
                current = tmp
            else:
                output.append(current.val)
                current = current.right
        return output

    def postorderTraversal(self, root):
        output = []
        stack = []

        while len(stack) > 0 or root:

            while root:
                stack.append(root)
                if root.left:
                    root = root.left
                else:
                    root = root.right

            node = stack.pop()
            output.append(node.val)
            if len(stack) > 0 and stack[-1].left == node:
                root = stack[-1].right

        return output

    # Doesn't work but don't know why
    def postorderTraversal(self, root):
        output = []
        stack = [root]
        node = root

        if node == None:
            return []

        while len(stack) > 0:

            append_flag = True

            node = stack.pop()

            if (node.left == None or node.left.val in output) and (node.right == None or node.right.val in output):
                append_flag = False

            if append_flag:
                stack.append(node)

                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            else:
                output.append(node.val)

        return output

root = TreeNode(1)
level1_right = TreeNode(2)
level2_left = TreeNode(3)

root.right = level1_right
level1_right.left = level2_left

s = Solution()
result = s.preorderTraversal(root)
print(result)