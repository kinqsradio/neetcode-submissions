class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, v in enumerate(nums):
            complementary = target - v
            if complementary in hash_map:
                return [hash_map[complementary], i]
            hash_map[v] = i

        return []