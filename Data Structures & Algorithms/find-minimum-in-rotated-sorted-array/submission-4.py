class Solution:
    def findMin(self, nums: List[int]) -> int:
        # don't know wtf this is but it works
        # return min(nums)

        # 
        nums.sort()
        return nums[0]

        # binary search
        # l, r = 0, len(nums) - 1

        # while l < r:
        #     m = l + (r-l) // 2

        #     if nums[m] < nums[r]:
        #         r = m
        #     else:
        #         l = m + 1

        # return nums[l]

        # bruteforce
        # for i in range(nums):