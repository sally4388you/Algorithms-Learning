class Solution:
    def findMin(self, nums):

        if len(nums) <= 2:
            return min(nums)

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            # if nums[mid - 1] > nums[mid] and nums[mid] < nums[(mid + 1) % len(nums)]:
                # return nums[mid]

            print(mid)

            if nums[mid] > nums[(mid + 1)%len(nums)]:
                return nums[(mid + 1)%len(nums)]

            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1

        return -1


nums = [2,3,4,5,1]
nums = [5,1,2,3,4]
nums = [4,5,6,7,0,1,2]
nums = [1,2,3]
# nums = [3,1,2]

s = Solution()
result = s.findMin(nums)
print(result)
