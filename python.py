cvcx# 1. list comprehesion
l = [x for x in nums if True]

# 2. extended slices
[start:stop:step]

# 3. lambda function: lambda x : expression
k = sorted(k, key = lambda x: x[0])

# 4. stack extend
stack.extend()

# 5. queue
from collections import deque
queue = deque([src])
queue.popleft()
queue.append()

# 6. priority queue
# https://docs.python.org/3/library/heapq.html
import heapq
heap = []
heapq.heappush(heap, (-dist(pt), pt))
heapq.heappop(heap)

# 7. set
s = set()
s.add()

# 8. dictionary
d = {}
d.get(x, 0)
next(iter(d))

# 9. deep copy
copy = L[:]

# 10. binary search
idx = bisect_left(array, num)

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

