**Intuition**

This problem can easily be modeled as a dynamic programming problem on graphs. What does a dynamic programming problem entail?

It has a recursive structure.
A bunch of choices to explore at each step.
Use the optimal solutions for sub-problems to solve top-level problems.
A base case.
This problem fits the bill. We have a dedicated start and endpoint. We have a bunch of choices for each node in the form of its neighbors. And, we want to minimize the overall shortest distance from the source to the destination which can be represented as a recursive structure in terms of shortest distances of its neighbors to the destination. So, we can apply a dynamic programming approach to solve this problem. We'll look at a recursive implementation here with memoization first and then talk about the iterative approach as well.

As with any recursive approach, we need to figure out the state of recursion. There are two parameters here which will control our recursion. One is obviously the node itself. The other is the number of steps. Let's call our recursion function recurse and define what the state of recursion looks like. \text{recurse}(\text{node},\text{stops})recurse(node,stops) will basically return the shortest distance for us to reach the destination from \text{node}node considering that there are stops left. This being said, it's easy to figure out what the top-level problem would be. It would be \text{recurse}(\text{0},\text{K})recurse(0,K).

Let's consider the following graph to understand why memoization (or caching) is required here.
![img5](https://leetcode.com/problems/cheapest-flights-within-k-stops/Figures/787/img5.png)

Say we start the source node A and build our recursion tree from there. There are two possible routes of getting to the node C with exactly 2 stops. Let's look at what these are.
![img6](https://leetcode.com/problems/cheapest-flights-within-k-stops/Figures/787/img6.png)

While the cost of these two paths is different, once we are at the node C, we have 2 steps less than what we had when we started off from the source node A. Our recursion representation doesn't care about the path you took to get to a node. It is about the shortest (cheapest) path from the current node with the given number of steps to get to a destination. In that sense, both these scenarios are exactly the same because both lead us to the same recursion state which is (\text{recurse}(\text{C}, \text{K-2}))(recurse(C,K-2)) and hence, the result for this recursion state can be cached or memoized.

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
