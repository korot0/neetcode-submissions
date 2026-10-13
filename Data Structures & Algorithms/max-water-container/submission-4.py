class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currentMostWater = 0
        left, right = 0, len(heights) - 1

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            unitsOfWater = width * height
            
            currentMostWater = max(currentMostWater, unitsOfWater)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return currentMostWater