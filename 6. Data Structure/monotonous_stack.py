# Monotonous Stack:
# The elements in the an monotonous increase stack keeps an increasing order.

# 907. Sum of Subarray Minimums
# https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step
# https://lh3.googleusercontent.com/-GyygvrTJ3GY/XRlvmDTxEHI/AAAAAAAAO4E/yDc-Xvo3isgM8QFOSiVp6yUK_j9E8cwGACK8BGAs/s0/2019-06-30.jpg

class Solution(object):

    def sumSubarrayMins(self, arr):
        
        # Monotonic Stack
        n = len(arr)
        left, right = [], []
        # Previous Less Element; Next Less Element
        in_stk_p, in_stk_n = [], []
        
        for i in range(n):
            left.append(i + 1)
            right.append(n - i)

        for i in range(n):
            # Previous Less Element
            while in_stk_p and in_stk_p[-1][0] > arr[i]:
                in_stk_p.pop()
                
            left[i] = i - in_stk_p[-1][1] if in_stk_p else i + 1
            in_stk_p.append((arr[i], i))
                
            # Next Less Element
            while in_stk_n and in_stk_n[-1][0] > arr[i]:
                x = in_stk_n.pop()
                right[x[1]] = i - x[1]
                
            in_stk_n.append((arr[i], i))
            
        ans, mod = 0, 10 ** 9 + 7
        for i in range(n):
            ans += arr[i] * left[i] * right [i]
            ans = ans % mod
            
        return ans


arr = [3,1,2,4] # 17
arr = [11,81,94,43,3] # 444
arr = [2,9,7,8,3,4,6,1]

solution = Solution()
result = solution.sumSubarrayMins(arr)
print(result)