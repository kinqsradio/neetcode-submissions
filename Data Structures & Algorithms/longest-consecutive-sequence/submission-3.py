class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        left = 0
        best = 1
        duplicate_count = 0

        for right in range(1, len(nums)):
            if nums[right] == nums[right - 1]:
                # Skip duplicates
                duplicate_count += 1
                continue
            if nums[right] == nums[right - 1] + 1:
                # Still consecutive
                best = max(best, right - left - duplicate_count + 1)
            else:
                # Sequence breaks, move left pointer
                left = right
                duplicate_count = 0

        return best