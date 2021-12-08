# https://leetcode.com/problems/range-sum-query-2d-mutable/solution/
class BinaryIndexedTree:

    def __init__(self, nums, build = True):

        # initialize all entries in bit array to 0
        self.bit = [0] * len(nums)
        # given nums array (ASSUME 1-based indexing)
        self.nums = nums
        # size of nums array
        self.n = len(nums)

        if build:
            self.buildBIT()


    def buildBIT(self):
        for k in range(1, self.n):
            val = self.nums[k]
            self.updateBIT(k, val)


    def updateBIT(self, i, val):
        # keep adding lsb(i) to i and add val to bit[i]
        while i < self.n:
            self.bit[i] += val
            i += self.lsb(i)


    def queryBIT(self, i):
        _sum = 0
        while i > 0:
            _sum += self.bit[i]
            i -= self.lsb(i)
        
        return _sum


    def query(self, i, j):
        return self.queryBIT(j) - self.queryBIT(i - 1)


    def update(self, i, val):
        old_val = self.query(i, i)
        diff = val - old_val
        self.updateBIT(i, diff)
        return


    def lsb(self, n):
        # the line below allows us to directly capture the right most non-zero bit of a number
        return n & (-n)


class Solution:
    def countSmaller(self, nums):

        offset = 10**4  # offset negative to non-negative
        size = 2 * 10**4 + 2  # total possible values in nums plus one dummy
        result = []

        BIT = BinaryIndexedTree([0] * size, False)

        for num in reversed(nums):
            result.append(BIT.queryBIT(num + offset))
            BIT.update(num + offset + 1, 1)
        return list(reversed(result))


nums = [0,2,3,1,2,4,1,2,3]

BIT = BinaryIndexedTree(nums)
print(BIT.bit)
print(BIT.queryBIT(7)) # 15
print(BIT.query(1, 4)) # 8


# Leetcode 315
nums = [5,2,6,1]
nums = [7,2,5,4,1,6]

s = Solution()
result = s.countSmaller(nums)
print(result)



