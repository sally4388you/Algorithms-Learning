# Longest Panlindrome Substring
class Solution:
    def manacher(self, s) :

        if len(s) == 0:
            return ""

        # T = self.preProcess(s)
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        # Center and Radius
        C = R = 0

        for i in range(1, n - 1):

            i_mirror = 2 * C - i

            # if: i is still in the range of the previous palindrome, it will take the full value of precomputed P[i_mirror]
            # else: it will take the rest that is in the range (R - i)
            P[i] = min(R - i, P[i_mirror]) if R > i else 0

            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > R:
                C = i
                R = i + P[i]


        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))

        # maxLen = centerIndex = 0
        # for i in range(1, n - 1):
        #     if P[i] > maxLen:
        #         maxLen = P[i]
        #         centerIndex = i

        return s[(centerIndex - maxLen) // 2 : (centerIndex + maxLen) // 2]

    def preProcess(self, s):

        sb = []

        for c in s:
            sb.extend('#' + c)

        sb.extend('#$')

        return sb


string = "abc"
string = "aaa"
string = "abaabc"

s = Solution()
result = s.manacher(string)
print(result)
