class Solution:
    def characterReplacement(self, s, k):
        d = {}
        dist = [0] * len(s)

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i

            dist[i] = i - d[s[i]]
            d[s[i]] = i

        for i in range(len(s)):
            ;

        return dist

        return 0


_s = "ABAB"
k = 2

s = Solution()
result = s.characterReplacement(_s, k)
print(result)
