import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None

        right = self.reverseList(right)
        left = head

        while right:
            tmp_l = left.next
            tmp_r = right.next

            left.next = right
            right.next = tmp_l

            left = tmp_l
            right = tmp_r
    
    def reverseList(self, head):
        node = head
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp

        return prev


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Solution()
s.reorderList(node1)

node = node1
while node:
    print(node.val)
    node = node.next