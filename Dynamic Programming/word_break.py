class Solution:

    def wordBreak(self, s, wordDict):

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):

            if s[:i] in wordDict:
                dp[i] = True
                continue

            for j in range(i - 1, -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]

    def wordBreak_brute_force(self, s, wordDict):

        if s in wordDict:
            return True

        for i in range(len(s)):
            if s[:i+1] in wordDict and self.wordBreak(s[i+1:], wordDict):
                return True

        return False

s = Solution()
wordDict = ["cats", "dog", "sand", "and", "cat"]
result = s.wordBreak("catsandog", wordDict)

# wordDict = ["apple", "pen"]
# result = s.wordBreak("applepenapple", wordDict)

# wordDict = ["leet", "code"]
# result = s.wordBreak("leetcode", wordDict)

print(result)