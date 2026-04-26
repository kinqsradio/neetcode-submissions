class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        result = 0
        min_height = min(heights[l], heights[r])

        while l<r:
            # We first find the min height of the pointer
            min_height = min(heights[l], heights[r])

            # Calculate the area that it can hold
            area = min_height * (r-l)

            # Update to find the max area
            result = max(result, area)
            
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1

        return result
