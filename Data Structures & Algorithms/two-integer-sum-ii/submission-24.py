class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 pointers
        # numbers.sort()

        # l, r = 0, len(numbers)-1
        # result = []

        # while l < r:
        #     s = numbers[l] + numbers[r] 
        #     if s > target:
        #         r-=1
        #     elif s < target:
        #         l+=1
        #     if s == target:
        #         return [l+1, r+1]
        
        # return []

        # bruteforce
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return[i+1, j+1]
        
        return []