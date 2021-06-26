# Definition for singly-linked list.
from Queue import PriorityQueue

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        size = len(lists)

        for i in range(0, math.ceil(math.log2(size))):
            step = 2 ** i
            start = 0
            while (start + step) < size:
                l1 = lists[start]
                l2 = lists[start + step]
                lists[start] = self.merge(l1, l2)
                start += step * 2

        return lists[0]

    def merge(self, l1, l2):
        node = dummy = ListNode(None)

        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        node.next = l1 or l2

        return dummy.next

    def mergeKLists_priority_queue(self, lists):
        head = point = ListNode(0)
        q = PriorityQueue()
        for i, l in enumerate(lists):
            if l:
                q.put((l.val, i, l))
        while not q.empty():
            val, i, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, i, node))
        return head.next


nodeA_1 = ListNode(1)
nodeA_2 = ListNode(4)
nodeA_3 = ListNode(5)

nodeB_1 = ListNode(1)
nodeB_2 = ListNode(3)
nodeB_3 = ListNode(4)

nodeC_1 = ListNode(2)
nodeC_2 = ListNode(6)

nodeA_1.next = nodeA_2
nodeA_2.next = nodeA_3

nodeB_1.next = nodeB_2
nodeB_2.next = nodeB_3

nodeC_1.next = nodeC_2


s = Solution()
node = s.mergeKLists([nodeA_1, nodeB_1, nodeC_1])

while node:
    print(node.val)
    node = node.next