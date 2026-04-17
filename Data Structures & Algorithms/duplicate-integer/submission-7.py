class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # BruteFroce
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

        # Hashmap 1
        # hash_map = {}
        # for i in nums:
        #     if i in hash_map:
        #         return True
        #     hash_map[i] = i
        # return False

        # Hashmap 2
        # count = defaultdict(int)
        # for num in nums:
        #     count[num] += 1
        #     if count[num] > 1:
        #         return True
        # return False
