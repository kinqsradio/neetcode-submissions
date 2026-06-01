class Solution:
    def trap(self, height: List[int]) -> int:
        # bruteforce
        # if not height: return 0
        # result = 0
        # for i in range(len(height)):
        #     leftMax = rightMax = height[i]

        #     for j in range(i):
        #         leftMax = max(leftMax, height[j])
        #     for j in range(i+1, len(height)):
        #         rightMax = max(rightMax, height[j])
        #     result += min(leftMax, rightMax) - height[i]
        # return result

        # 2 pointers
        if not height: return 0

        l, r = 0, len(height)-1
        res = 0
        maxLeft, maxRight = height[l] , height[r]
        while l<r: 
            if maxLeft < maxRight:
                l+=1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
            else:
                r-=1
                maxRight = max(maxRight, height[r])
                res+= maxRight - height[r]
        return res