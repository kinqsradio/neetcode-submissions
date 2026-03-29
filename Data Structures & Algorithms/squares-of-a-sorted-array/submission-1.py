class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        result = []

        while l <= r:
            squareL = nums[l] * nums[l]
            squareR = nums[r] * nums[r]

            if squareL > squareR:
                result.append(squareL)
                l += 1
            else:
                result.append(squareR)
                r -= 1
        
        return result[::-1]