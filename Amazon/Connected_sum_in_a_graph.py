# https://leetcode.com/discuss/interview-question/1256258/Connected-sum-in-a-graph-or-Amazon-OA

import math

class Solution:
    def connectedSum(self, n, edges):

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
            
        def union(xy):
            x, y = list(map(find, xy))
            if rank[x] < rank[y]:
                parent[x] = y
                rank[y] += 1
            else:
                parent[y] = x
                rank[x] += 1
                if rank[x] == rank[y]:
                    rank[x] += 1
        
        parent, rank = [_ for _ in range(n)], [1] * n
        list(map(union, edges))

        parent = set([find(x) for x in parent])
        res = 0

        for i in parent:
            res += math.ceil(math.sqrt(rank[i]))

        return res



n = 10
edges = [[1,2], [1,3], [2,4], [3,5], [7,8]]


s = Solution()
result = s.connectedSum(n, edges)
print(result) # 8



