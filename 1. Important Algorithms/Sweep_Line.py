# 370. Range Addition
class Solution:
    def getModifiedArray(self, length, updates):
        
        # sweep line
        ans = [0] * length
        
        for start, end, val in updates:
            ans[start] += val
            if end < length - 1:
                ans[end + 1] -= val
                
        for i in range(1, len(ans)):
            ans[i] = ans[i] + ans[i - 1]
        
        return ans

length = 5
updates = [[1,3,2],[2,4,3],[0,2,-2]]

solution = Solution()
result = solution.getModifiedArray(length, updates)
print(result)