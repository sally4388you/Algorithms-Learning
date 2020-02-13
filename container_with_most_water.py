class Solution:
    def maxArea(self, height) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while (left < right) :
            distance = right - left
            if (height[left] <= height[right]) :
                smaller_bar = height[left]
                left += 1
            else :
                smaller_bar = height[right]
                right -= 1

            max_area = max(max_area, smaller_bar * distance)

        return max_area

s = Solution()
height = [1,8,6,2,5,4,8,3,7]
result = s.maxArea(height)
print(result)