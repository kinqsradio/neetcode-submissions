class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers.sort()

        l, r = 0, len(numbers)-1
        result = []

        while l < r:
            s = numbers[l] + numbers[r] 
            if s > target:
                r-=1
            elif s < target:
                l+=1
            if s == target:
                return [l+1, r+1]
        
        return []