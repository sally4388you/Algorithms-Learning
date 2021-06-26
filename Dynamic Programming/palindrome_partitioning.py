class Solution:

    def getIsPalindrome(self, s):

        isPalindrome = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            isPalindrome[i][i] = True

        for i in range(len(s) - 1):
            isPalindrome[i][i + 1] = s[i] == s[i + 1]

        for length in range(2, len(s)):
            for start in range(0, len(s) - length):
                isPalindrome[start][start + length] = isPalindrome[start + 1][start + length - 1] and s[start] == s[start + length]

        return isPalindrome


    def minCut(self, s):

        if not s or len(s) <= 0:
            return 0

        isPalindrome = self.getIsPalindrome(s)

        count = [len(s)] * (len(s) + 1)
        count[0] = 0

        for i in range(1, len(s) + 1):
            count[i] = i
            # j determines where to cut
            # then you decide whether cutting at position j is the best solution
            for j in range(1, i + 1):
                # Solution from video
                # if isPalindrome[i - j][i - 1]:
                    # count[i] = min(count[i], count[i - j] + 1)

                if isPalindrome[j - 1][i - 1]:
                    count[i] = min(count[i], count[j - 1] + 1)

        return count[len(s)] - 1

    def minCut_short(self, s):
        if s == s[::-1]:
            return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1

        dp = [x for x in range(-1, len(s))]
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]


s = Solution()
result = s.minCut('abbab')

print(result)