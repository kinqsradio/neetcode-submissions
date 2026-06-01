class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # bruteforce
        # if not nums:
        #     return 0

        # numSet = set(nums) 
        # longest = 0

        # for n in nums:
        #     streak, curr = 0, n
        #     while curr in numSet:
        #         streak += 1
        #         curr += 1
        #     longest = max(longest, streak)
        
        # return longest

        # sorting
        # if not nums: return 0
        # res = 0
        # nums.sort()

        # curr, streak = nums[0], 0
        # i = 0
        # while i < len(nums):
        #     if curr!= nums[i]:
        #         curr = nums[i]
        #         streak = 0


        #     while i < len(nums) and nums[i] == curr:
        #         i+=1
        #     streak += 1
        #     curr += 1
        #     res =max(res, streak)
        # return res

        # hashset
        numSet = set(nums)
        longest = 0
        for num in nums:
            if (num-1) not in numSet:
                length = 1
                while (num+length) in numSet:
                    length += 1
                longest=max(length, longest)
        return longest