class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash_map = {}
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in hash_map:
        #         return [hash_map[diff], i]
        #     hash_map[nums[i]] = i

        # return []

        
        hash_map = {}
        for i in range(len(nums)):
            complimentary = target - nums[i]
            if complimentary in hash_map:
                return [hash_map[complimentary], i]
            hash_map[nums[i]] = i
        return []