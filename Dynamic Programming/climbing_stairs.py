import math

class Solution:
    def climbStairs(self, n):

        matrix = [0] * (n + 1)

        for i in range(1, n + 1):
            if i <= 2:
                matrix[i] = i
            else:
                matrix[i] = matrix[i-1] + matrix[i-2]
        
        return matrix[n]

    def fibonacci_number(self, n):
        if n <= 2:
            return n

        prev1 = 1
        prev2 = 2
        for i in range(3, n + 1):
            result = prev1 + prev2
            prev1 = prev2
            prev2 = result

        return result

    def fibonacci_fomula(self, n):
        sqrt5 = math.sqrt(5);
        fibn = pow((1 + sqrt5) / 2, n + 1) - pow((1 - sqrt5) / 2, n + 1);
        return (int)(fibn / sqrt5);
        

s = Solution()
result = s.fibonacci_fomula(5)

print(result)