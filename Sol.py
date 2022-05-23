class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        maxarea = 0

        while (left != right):

            selected_area = min(height[left], height[right]) * (right - left)

            maxarea = max(maxarea, selected_area)

            if (height[left] > height[right]):
                right -= 1
            else:
                left += 1

        return maxarea