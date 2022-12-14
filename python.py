# 1. list comprehesion
l = [x for x in nums if True]
dp = [[0] * len(grid[0]) for _ in range(len(grid))]

# 2. extended slices
[start:stop:step]

# 3. lambda function: lambda x : expression
# smaller -> bigger
k = sorted(k, key = lambda x: x[0])
k.sort(key = lambda x: x[0])
# sort by two keys. First by len(x) then x[1]
k.sort(key = lambda x: (len(x), x[1]))
# in reversed order
k.sort(key = lambda x: -x[0])
k.sort(key = lambda x: x[0], reverse = True)

# 4. stack extend
stack = [element]
stack.extend([e1, e2])

# 5. queue
from collections import deque
queue = deque([src])
# O(1)
queue.popleft()
queue.append()

# 6. priority queue (min heap)
# https://docs.python.org/3/library/heapq.html
import heapq
heap = []
# always pick the smallest distance
# O(log n)
heapq.heappush(heap, (distance, value))
heapq.heappush(heap, value)
# O(log n)
heapq.heappop(heap)
# The interesting property of a heap is that heap[0] is always its smallest element.
smallest = heap[0]

# 7. set
s = set()
s.add()
s.update(list)

# 8. dictionary
d = {}
d.get(x, 0)
next(iter(d))
d.items = [(key, val)]

# 9. deep copy
copy = L[:]

# 10. binary search
from bisect import bisect_left
idx = bisect_left(array, num)
# num is greater than any element in array
idx == len(array)

# 11. OOP
# 1) encapsulation, abstraction
class Dog:

    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Replace .description() with __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


# 2) inherence
class Bulldog(Dog):
    # 3) polymorphism
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

buddy = Dog("Buddy", 9)


# 12. string to int
num = ord(s)


# 13. list to string
strings = ''.join(lists)

# 14. global variables
nonlocal last, first

# 15. for loop
for key, value in enumerate(values):
    print(key, value)

