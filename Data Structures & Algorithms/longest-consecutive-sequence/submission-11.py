class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums) 
        longest = 0

        for n in nums:
            streak, curr = 0, n
            while curr in numSet:
                streak += 1
                curr += 1
            longest = max(longest, streak)
        
        return longest