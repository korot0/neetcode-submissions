class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        currentMostWater = 0
        left, right = 0, n - 1

        for i in range(n):
            width = right - left
            if width == 0:
                break
            height = min(heights[left], heights[right])
            unitsOfWater = width * height
            
            if unitsOfWater > currentMostWater:
                currentMostWater = unitsOfWater

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return currentMostWater