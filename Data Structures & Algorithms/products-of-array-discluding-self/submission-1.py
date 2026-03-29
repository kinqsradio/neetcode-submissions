class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def product(nums: List[int]) -> int:
            result = 1
            for n in nums:
                result *= n
            
            return result

        result = [1] * len(nums)

        i = 0
        while i < len(nums):
            print(f"Current list: {nums}")
            print(f"Computing index {i}: excluding nums[{i}] = {nums[i]}")

            prefix = product(nums[:i])
            suffix = product(nums[i + 1:])
            print(
                f"Expression: product(nums[:{i}])={prefix} * "
                f"product(nums[{i + 1}:])={suffix} = {prefix * suffix}"
            )

            result[i] *= prefix * suffix
            i += 1

        return result  