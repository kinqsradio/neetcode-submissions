class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return nums.index(target) if target in nums else -1

        # binary
        # l, r = 0, len(nums) - 1

        # while l <= r:
        #     mid = (l+r) // 2
        #     if target == nums[mid]:
        #         return mid

        #     if nums[l] <= nums[mid]:
        #         if target > nums[mid] or target < nums[l]:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     else:
        #         if target < nums[mid] or target > nums[r]:
        #             r = mid -1
        #         else:
        #             l = mid + 1

        # return -1
        
        # bruteforce
        for i in range(len(nums)):
            if target == nums[i]:
                return i
        return -1