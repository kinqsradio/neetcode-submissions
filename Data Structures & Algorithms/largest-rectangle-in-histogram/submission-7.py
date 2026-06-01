class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 2 pointers
        # maxArea = 0
        # for l in range(len(heights)):
        #     minHeight = float('inf')
        #     for r in range(l, len(heights)): 
        #         rHeight = heights[r]
        #         minHeight = min(minHeight, rHeight)
        #         width = r - l + 1
        #         area = minHeight * width
        #         maxArea = max(area, maxArea)
        
        # return maxArea

        # Stack
        maxArea = 0

        stack = []
        leftMost = [-1] * len(heights)
        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)

        stack = []
        rightMost = [len(heights)] * len(heights)
        for i in range(len(heights) -1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)

        for i in range(len(heights)):
            leftMost[i] += 1
            rightMost[i] -= 1
            area = heights[i] * (rightMost[i] - leftMost[i] + 1)
            maxArea = max(maxArea, area)


        return maxArea