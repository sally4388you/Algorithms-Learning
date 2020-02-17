class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        node = head
        prev = None
        while node:
            tmp = node.next

            node.next = prev

            prev = node
            node = tmp

        return prev

    def reverseList_recursion(self, head):
        if not head or not head.next:
            return head

        node = self.reverseList_recursion(head.next)

        head.next.next = head
        head.next = None

        return node


    def reverseBetween(self, head, m, n):

        count = 0
        dummy = ListNode(0)
        dummy.next = head

        p = dummy
        while m > 1:
            m = m - 1
            n = n - 1
            p = p.next

        prev = p
        node = p.next
        tail = node

        while n > 0:
            tmp = node.next

            node.next = prev

            prev = node
            node = tmp
            n = n - 1

        p.next = prev
        tail.next = node

        return dummy.next

    def reverseBetween_recursion(self, head, m, n):
        
        if not head:
            return None

        left, right = head, head
        stop = False
        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers     
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next

        recurseAndReverse(right, m, n)
        return head

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
node = s.reverseBetween(node1, 1, 4)

while node:
    print(node.val)
    node = node.next