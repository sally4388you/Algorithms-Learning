class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList_recursion(self, head):

        def recursion(head, count):
            if head is None or count <= 1:
                if head:
                    head.next = None
                return head

            mid = count // 2

            p = head
            n = 0
            while p is not None and n < mid:
                p = p.next
                n += 1

            L = recursion(head, mid)
            R = recursion(p, count - mid)

            return_head = p = ListNode(None)
            while L is not None and R is not None:
                if L.val < R.val:
                    p.next = L
                    L = L.next
                else:
                    p.next = R
                    R = R.next
                p = p.next

            p.next = L or R

            return return_head.next

        count = 0
        p = head
        while p is not None:
            count += 1
            p = p.next

        head = recursion(head, count)

        return head

    # O(nlogn) time O(1) space
    def sortList(self, head):
        def getSize(head):
            counter = 0
            node = head
            while node:
                node = node.next
                counter +=1
            return counter

        def split(head, step):
            for i in range(1, step):
                if head:
                    head = head.next
                else:
                    break

            if not head:
                return None

            temp, head.next = head.next, None
            return temp

        def merge(l, r, head):
            cur = head
            while l and r:
                if l.val < r.val:
                    cur.next, l = l, l.next
                else:
                    cur.next, r = r, r.next
                cur = cur.next

            cur.next = l or r
            while cur.next:
                cur = cur.next

            return cur

        # main
        if head is None:
            return None

        size = getSize(head)
        dummy = ListNode(None)
        dummy.next = head

        for i in range(1, math.ceil(math.log2(size))):
            cur = dummy.next
            tail = dummy
            step = 2**i
            while cur:
                l = cur
                r = split(l, step)
                cur = split(r, step)
                tail = merge(l, r, tail)

        return dummy.next


node1 = ListNode(-1)
node2 = ListNode(5)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(0)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Solution()
node = s.sortList(node1)

while node:
    print(node.val)
    node = node.next
