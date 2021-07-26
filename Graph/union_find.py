class DSUBasic:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset != yset:
            self.parent[xset] = self.parent[yset]

        return


class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return
        if self.rank[xset] > self.rank[yset]:
            self.parent[yset] = self.parent[xset]
        elif self.rank[xset] < self.rank[yset]:
            self.parent[xset] = self.parent[yset]
        else:
            self.parent[xset] = self.parent[yset]
            self.rank[yset] += 1


class Solution:

    # Longest Consecutive Sequence
    # Number of Provinces
    def basic(self, isConnected):

        N = len(isConnected)
        dsu = DSU(N)
        for i in range(1, N):
            for j in range(i):
                if isConnected[i][j] == 1:
                    dsu.union(i, j)
        
        parent = set()
        for p in dsu.parent:
            parent.add(dsu.find(p))
        return len(parent)

    # Number of Connected Components
    def unionByRank(self, n, edges):
        dsu = DSU(n)
        for edge in edges:
            dsu.union(edge[0], edge[1])
        
        parent = set()
        for i in range(n):
            parent.add(dsu.find(i))
        return len(parent)

 
s = Solution()

# Number of Provinces
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
result = s.basic(isConnected)
print(result)


# Number of Connected Components
n = 5
edges = [[0,1],[1,2],[2,3],[3,4]]
result = s.unionByRank(n, edges)
print(result)

