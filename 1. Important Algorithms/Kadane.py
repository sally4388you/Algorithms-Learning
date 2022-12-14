# Maximum Subarray Sum
class Solution:
    def maxSubArray(self, nums):
        best_sum = current_sum = nums[0]
        
        for x in nums:
            current_sum = max(x, current_sum + x)
            best_sum = max(best_sum, current_sum)
        return best_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [-1,-2,-3]

s = Solution()
result = s.maxSubArray(nums)
print(result)