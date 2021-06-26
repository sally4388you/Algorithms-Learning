import math

class Solution:

    def iteration(self, nums, target):
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = math.ceil((right - left) / 2) + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def another_iteration(self, num, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            
            mid = (left + right) // 2
            if target > self.num[mid]:
                left = mid + 1
            else:
                right = mid

        return left

    def recursion(self, nums, target):
        return self.binarysearch(nums, 0, len(nums) - 1, target)

    def binarysearch(self, nums, left, right, target):
        mid = math.ceil((right - left) / 2) + left

        if right < left:
            return -1
        elif nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarysearch(nums, mid + 1, right, target)
        else:
            return self.binarysearch(nums, left, mid - 1, target)


s = Solution()
nums = [1,5]
target = 1


result = s.iteration(nums, target)
print(result)