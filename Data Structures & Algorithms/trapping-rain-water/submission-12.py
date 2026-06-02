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

        # 2 Pointers
        if not height: return 0
        l, r = 0, len(height)-1
        res = 0 
        lMax, rMax = height[l], height[r]
        while l<r:
            if lMax < rMax:
                l+=1
                lMax = max(lMax, height[l])
                res += lMax - height[l]
            else:
                r-=1
                rMax = max(rMax, height[r])
                res += rMax - height[r]
        return res