class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # BruteForce
        # n = len(nums)
        # for num in nums:
        #     count = sum(1 for i in nums if i == num)
        #     if count > n // 2:
        #         return num
        
        # Sorting
        nums.sort()
        return nums[len(nums)//2]