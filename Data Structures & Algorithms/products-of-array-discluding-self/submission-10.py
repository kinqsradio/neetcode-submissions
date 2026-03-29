class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def product(nums: List[int]) -> int:
            result = 1
            for n in nums:
                result *= n
            
            return result

        left = 0
        right = len(nums) - 1
        result = [1] * len(nums)

        while left < len(nums) and right >= 0:
            if left < right:
                result[left] *= product(nums[:left]) * product(nums[left + 1:])
                result[right] *= product(nums[:right]) * product(nums[right + 1:])
            elif left == right:
                # result[left] *= product(nums[:left]) * product(nums[left + 1:])
                result[right] *= product(nums[:right]) * product(nums[right + 1:])

            
            left += 1
            right -= 1

        return result  