class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2 pointers
        # l,r = 0, len(heights)-1
        # result = 0
        # min_height = min(heights[l], heights[r])

        # while l<r:
        #     # We first find the min height of the pointer
        #     min_height = min(heights[l], heights[r])

        #     # Calculate the area that it can hold
        #     area = min_height * (r-l)

        #     # Update to find the max area
        #     result = max(result, area)
            
        #     if heights[l] <= heights[r]:
        #         l+=1
        #     else:
        #         r-=1

        # return result

        # bruteforce
        result = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                result = max(result, min(heights[i], heights[j])* (j-i))
        return result