# Loop Detection
# Find the Duplicate Number

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare

    def loopDetection(self, head):
        fast = slow = head
        # Find collision spot. This will be LOOP_SIZE - k steps into the linked list
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # Error check - No meeting point, and therefore no loop
        if fast == None or fast.next == None:
            return None

        # Move slow to head. Keep fast at Meeting Point. Each are k steps from the Loop Start. If they move at the same pace, they must meet at Loop Start
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

nums = [1,3,4,2,2]
nums = [3,1,3,4,2]

s = Solution()
result = s.findDuplicate(nums)
print(result)