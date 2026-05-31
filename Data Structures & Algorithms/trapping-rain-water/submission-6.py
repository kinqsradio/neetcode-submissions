class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 pointers
        # if not height: return 0

        # l, r = 0, len(height) - 1
        # rightMaxleftMax,  = height[l], height[r]
        # res = 0
        # while l<r:
        #     if leftMax < rightMax:
        #         l += 1
        #         leftMax = max(leftMax, height[l])
        #         res += leftMax - height[l]
        #     else:
        #         r -= 1
        #         rightMax = max(rightMax, height[r])
        #         res += rightMax - height[r]
        # return res if height else 0

        # bruteforce
        if not height: return 0
        result = 0
        for i in range(len(height)):
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i+1, len(height)):
                rightMax = max(rightMax, height[j])
            result += min(leftMax, rightMax) - height[i]
        return result