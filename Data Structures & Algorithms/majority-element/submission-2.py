class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # BruteForce
        # n = len(nums)
        # for num in nums:
        #     count = sum(1 for i in nums if i == num)
        #     if count > n // 2:
        #         return num
        
        # Sorting
        # nums.sort()
        # return nums[len(nums)//2]

        # Hashmap
        count = defaultdict(int)
        res = maxCount = 0
        for num in nums:
            count[num] += 1
            if maxCount < count[num]:
                res = num
                maxCount = count[num]
        return res