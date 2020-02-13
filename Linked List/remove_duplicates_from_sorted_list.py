class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates_1(self, head):
        if head == None:
            return head

        prev = head
        node = head.next
        while node:
            if prev.val == node.val:
                prev.next = node.next
            else:
                prev = prev.next
            node = node.next

        return head

    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        fast = head
        slow = dummy

        while fast:
            while fast.next and fast.next.val == fast.val:
                fast = fast.next

            if slow.next != fast:
                slow.next = fast.next
                fast = slow.next
            else:
                slow = slow.next
                fast = fast.next

        return dummy.next

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)
node4 = ListNode(2)
node5 = ListNode(3)
# node6 = ListNode(4)
# node7 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# node5.next = node6
# node6.next = node7

s = Solution()
node = s.deleteDuplicates(node1)

while node:
    print(node.val)
    node = node.next