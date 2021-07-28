# Longest Panlindrome
class Solution:
    def manacher(s) :

        if len(s) == 0:
            return ""

        T = preProcess(s)

        return T

        n = len(T)

        P = [0] * n

        C = R = 0

        for i in range(1, n - 1):

            i_mirror = 2 * C - i

            P[i] = min(R - i, P[i_mirror]) if R > i else 0

            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > R:
                C = i
                R = i + P[i]

        maxLen = centerIndex = 0

        for i in range(1, n - 1):
            if P[i] > maxLen:
                maxLen = P[i]
                centerIndex = i



        return s[(centerIndex - 1 - maxLen) // 2 : maxLen]



    def preProcess(s):

        sb = []

        for c in s:
            sb.extend('#' + c)

        sb.extend('#$')

        return sb


string = "abc"
string = "aaa"

s = Solution()
result = s.manacher(string)
print(result)
