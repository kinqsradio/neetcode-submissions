class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Hashmap
        # hash_map = {}
        # for i in nums:
        #     if i in hash_map:
        #         return True
        #     hash_map[i] = i
        # return False

        count = defaultdict(int)
        maxCount = 0
        for num in nums:
            count[num] += 1
            if count[num] > 1:
                return True
            # return False

        return False
