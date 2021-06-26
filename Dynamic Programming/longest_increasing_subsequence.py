class Solution:
    def lengthOfLIS(self, nums):
        dp = [1] * (len(nums) + 1)
        maxlen = 0

        for i in range(len(nums)):
            for j in range(i, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            maxlen = max(maxlen, dp[i])

        return maxlen

    def lengthOfLIS_binary_search(self, nums):

        def BinSearch(arr, x):

            i, j = 0, len(arr)

            while i != j:
                m = (i + j) // 2
                if arr[m] < x:
                    i = m + 1
                else:
                    j = m

            return i

        arr = []

        for i in nums:
            pos = BinSearch(arr, i)
            if pos == len(arr):
                arr.append(i)
            else:
                arr[pos] = i


        return len(arr)

s = Solution()
# result = s.lengthOfLIS([10,9,2,5,3,7,101,18])
result = s.lengthOfLIS_binary_search([10,9,2,5,3,7,101,18])
# result = s.lengthOfLIS([2, 2])

print(result)