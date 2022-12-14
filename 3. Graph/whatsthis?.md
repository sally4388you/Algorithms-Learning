**Intuition**

This problem can easily be modeled as a dynamic programming problem on graphs. What does a dynamic programming problem entail?

It has a recursive structure.
A bunch of choices to explore at each step.
Use the optimal solutions for sub-problems to solve top-level problems.
A base case.
This problem fits the bill. We have a dedicated start and endpoint. We have a bunch of choices for each node in the form of its neighbors. And, we want to minimize the overall shortest distance from the source to the destination which can be represented as a recursive structure in terms of shortest distances of its neighbors to the destination. So, we can apply a dynamic programming approach to solve this problem. We'll look at a recursive implementation here with memoization first and then talk about the iterative approach as well.

As with any recursive approach, we need to figure out the state of recursion. There are two parameters here which will control our recursion. One is obviously the node itself. The other is the number of steps. Let's call our recursion function recurse and define what the state of recursion looks like. recurse(node,stops) will basically return the shortest distance for us to reach the destination from node considering that there are stops left. This being said, it's easy to figure out what the top-level problem would be. It would be recurse(0,K).

Let's consider the following graph to understand why memoization (or caching) is required here.
![img5](https://leetcode.com/problems/cheapest-flights-within-k-stops/Figures/787/img5.png)

Say we start the source node A and build our recursion tree from there. There are two possible routes of getting to the node C with exactly 2 stops. Let's look at what these are.
![img6](https://leetcode.com/problems/cheapest-flights-within-k-stops/Figures/787/img6.png)

While the cost of these two paths is different, once we are at the node C, we have 2 steps less than what we had when we started off from the source node A. Our recursion representation doesn't care about the path you took to get to a node. It is about the shortest (cheapest) path from the current node with the given number of steps to get to a destination. In that sense, both these scenarios are exactly the same because both lead us to the same recursion state which is (recurse(C,K-2)) and hence, the result for this recursion state can be cached or memoized.

**Algorithm**

1. We'll define a function called recurse which will take two inputs: node and stops.

2. We'll also define a dictionary memo of tuples that will store the optimal solution for each recursion state encountered.

3. At each stage, we'll first check if we have reached the destination or not. If we have, then no more moves have to be made and we return a value of 0 since the destination is at a zero distance from itself.

4. Next, we check if we have any more stops left. If we don't then we return inf basically representing that we cannot reach the destination from the current recursion state.

5. Finally, we check if the current recursion state is cached in the memo dictionary and if it is, we return the answer right away.

6. If none of these conditions are met,we progress in our recursion. For that we will iterate over the adjacency matrix to obtain the neighbors for the current node and make a recursive call for each one of them. The node would be the neighboring node and the number of stops would incremeneted by 1.

7. To each of these recursion calls, we add the weight of the corresponding edge i.e.

recurse(neighbor, stops + 1) + weight(node, neighbor)

8. We need to return the result of recurse(src, 0) as the answer.

```Python
class Solution:
    
    def __init__(self):
        self.adj_matrix = None
        self.memo = {}
    
    def findShortest(self, node, stops, dst, n):
            
        # No need to go any further if the destination is reached    
        if node == dst:
            return 0
        
        # Can't go any further if no stops left
        if stops < 0:
            return float("inf")
        
        # If the result of this state is already cached, return it
        if (node, stops) in self.memo:
            return self.memo[(node, stops)]
        
        # Recursive calls over all the neighbors
        ans = float("inf")
        for neighbor in range(n):
            if self.adj_matrix[node][neighbor] > 0:
                ans = min(ans, self.findShortest(neighbor, stops-1, dst, n) + self.adj_matrix[node][neighbor])
        
        # Cache the result
        self.memo[(node, stops)] = ans        
        return ans
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        self.adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.memo = {}
        for s, d, w in flights:
            self.adj_matrix[s][d] = w
        
        result = self.findShortest(src, K, dst, n)
        return -1 if result == float("inf") else result
```

**Complexity Analysis**

Time Complexity: The time complexity for a recursive solution is defined by the number of recursive calls we make and the time it takes to process one recursive call. The number of recursive calls we can potentially make is O(V⋅K). In each recursive call, we iterate over a given node's neighbors. That takes time O(V) because we are using an adjacency matrix. Thus, the overall time complexity is O(V^2⋅K).
Space Complexity: (V⋅K+V^2) where O(V⋅K) is occupied by the memo dictionary and the rest by the adjacency matrix structure we build in the beginning.
