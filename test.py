import math

class Solution(object):

    def KMPSearch(self, text, pattern):
        
        lps = self.computeLPSArray(pattern)
        p1 = p2 = 0

        while p1 < len(text):
            if text[p1] == pattern[p2]:
                p1 += 1
                p2 += 1

                if p2 == len(pattern):
                    # found
                    print('found at ' + str(p1 - p2))
                    p2 = lps[p2 - 1]

            else:
                if p2 == 0:
                    p1 += 1
                else:
                    p2 = lps[p2 - 1]

        return

    def computeLPSArray(self, pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps


text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

solution = Solution()
result = solution.KMPSearch(text, pattern)
print(result)