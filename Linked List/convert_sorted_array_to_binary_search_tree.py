# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        
        head = self.recursion(nums, 0, len(nums))
        return head

    def recursion(self, nums, left, right):

        if right - 1 == left:
            head = TreeNode(nums[left])
            return head
        elif right == left:
            return None

        mid = left + (right - left) // 2

        head = TreeNode(nums[mid])
        head.left = self.recursion(nums, left, mid)
        head.right = self.recursion(nums, mid + 1, right)

        return head

s = Solution()
node = s.sortedArrayToBST([-10,-3,0,5,9])