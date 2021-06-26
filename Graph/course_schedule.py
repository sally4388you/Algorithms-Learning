class Solution:
    def canFinish(self, numCourses, prerequisites):

        def dfs(node):
            visited = self.visited.get(node, 0)

            # 2: permanent
            if visited == 2:
                return True

            # 1: temporary. not a DAG
            if visited == 1:
                return False

            self.visited[node] = 1

            for i in self.graph[node]:
                if not dfs(i):
                    return False

            self.visited[node] = 2
            # self.topological_sort.append(node)

            return True

        self.visited = {}
        self.graph = [[] for _ in range(numCourses)]
        # self.topological_sort = []

        for edge in prerequisites:
            self.graph[edge[1]].append(edge[0])

        for i in range(len(self.graph)):
            if not self.visited.get(i, 0):
                if not dfs(i):
                    return False

        return True

class GNode(object):
    """  data structure represent a vertex in the graph."""
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict, deque
        # key: index of node; value: GNode
        graph = defaultdict(GNode)

        totalDeps = 0
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].inDegrees += 1
            totalDeps += 1

        # we start from courses that have no prerequisites.
        # we could use either set, stack or queue to keep track of courses with no dependence.
        nodepCourses = deque()
        for index, node in graph.items():
            if node.inDegrees == 0:
                nodepCourses.append(index)

        removedEdges = 0
        while nodepCourses:
            # pop out course without dependency
            course = nodepCourses.pop()

            # remove its outgoing edges one by one
            for nextCourse in graph[course].outNodes:
                graph[nextCourse].inDegrees -= 1
                removedEdges += 1
                # while removing edges, we might discover new courses with prerequisites removed, i.e. new courses without prerequisites.
                if graph[nextCourse].inDegrees == 0:
                    nodepCourses.append(nextCourse)

        if removedEdges == totalDeps:
            return True
        else:
            # if there are still some edges left, then there exist some cycles
            # Due to the dead-lock (dependencies), we cannot remove the cyclic edges
            return False

s = Solution()
result = s.canFinish(3, [[0,1],[0,2],[1,2]])
print(result)
