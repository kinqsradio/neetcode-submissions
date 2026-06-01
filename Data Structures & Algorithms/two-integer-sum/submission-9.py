class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        # BruteForce
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
        
        # Hashmap
        # hash_map = {}
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in hash_map:
        #         return [hash_map[diff], i]
        #     hash_map[nums[i]] = i
        # return []

        hmap = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in hmap:
                return [hmap[diff], i]
            hmap[v] = i

        return []
        