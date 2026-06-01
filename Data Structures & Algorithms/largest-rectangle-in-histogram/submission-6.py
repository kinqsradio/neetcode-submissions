class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        for l in range(len(heights)):
            minHeight = float('inf')
            for r in range(l, len(heights)): 
                rHeight = heights[r]
                minHeight = min(minHeight, rHeight)
                width = r - l + 1
                area = minHeight * width
                maxArea = max(area, maxArea)
        
        return maxArea