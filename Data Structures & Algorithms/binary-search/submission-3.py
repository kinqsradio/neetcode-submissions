class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 2 pointers
        # l, r = 0, len(nums) -1

        # while l <= r:
        #     m = l + ((r-l) //2 )
        #     if nums[m] > target:
        #         r = m-1
        #     elif nums[m] < target:
        #         l = m+1
        #     else:
        #         return m

        # return -1

        # bruteforce
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1

        l, r = 0, len(nums) -1
        while l <= r:
            m = l + ((r-l) // 2)
            if nums[m] > target:
                r = m -1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1