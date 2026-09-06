class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:

            # Calculate area
            width = right - left
            h = min(height[left], height[right])
            area = width * h

            # Store maximum area
            result = max(result, area)

            # Move the smaller bar
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result
