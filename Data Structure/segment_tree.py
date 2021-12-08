# a tree data structure used for storing information about intervals, or segments

# https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/
class SegmentTreeByArr:

    def __init__(self, n):
        self.tree = [0] * (2 * n)
        self.size = n


    def query(self, start, end):
        start += self.size
        end += self.size
        res = 0

        while start <= end:
            # Is right node. Right nodes are odd numbers
            if start % 2 == 1:
                res += self.tree[start]
                start += 1

            # Is left node. Left nodes are even numbers
            if end % 2 == 0:
                res += self.tree[end]
                end -= 1

            start //= 2
            end //= 2

        return res


    def update(self, index):
        index += self.size
        # update from leaf to root
        self.tree[index] += 1
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]

        return


class SegmentTreeNode(object):
    def __init__(self, val, start, end):
        self.val = val
        self.start = start
        self.end = end
        self.left = self.right = None


class SegmentTree(object):
    def __init__(self, n):
        self.root = self.build(0, n - 1)

    def build(self, start, end):
        if start > end:
            return None

        root = SegmentTreeNode(0, start, end)
        if start == end:
            return root

        mid = (start + end) // 2
        root.left = self.build(start, mid)
        root.right = self.build(mid + 1, end)

        return root

    def update(self, nodeIdx, root=None):
        root = root or self.root
        if nodeIdx < root.start or nodeIdx > root.end:
            return root.val

        if nodeIdx == root.start == root.end:
            root.val += 1
            return root.val

        root.val = self.update(nodeIdx, root.left) + self.update(nodeIdx, root.right)
        return root.val

    def query(self, start, end, root=None):
        root = root or self.root
        if end < root.start or start > root.end:
            return 0

        if start <= root.start and end >= root.end:
            return root.val

        return self.query(start, end, root.left) + self.query(start, end, root.right)


class Solution:
    def countSmaller(self, nums):

        # so that it doesn't need to create 10 ** 4 nodes but just n nodes.
        d = {val: idx for idx, val in enumerate(sorted(set(nums)))}

        # tree, result = SegmentTree(len(d)), []
        tree, result = SegmentTreeByArr(len(d)), []
        for i in range(len(nums) - 1, -1, -1):
            result.append(tree.query(0, d[nums[i]] - 1))
            tree.update(d[nums[i]])
            
        return result[::-1]


nums = [5,2,6,1]

nums = [7,2,5,4,1,6]

# nums = [-1]

# nums = [-1,-1]

s = Solution()
result = s.countSmaller(nums)
print(result)

