class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, v in enumerate(nums):
            # i > 0 means it isnt the first value in the array
            if i > 0 and v == nums[i-1]: #v == nums[i-1] => This eliminate duplicate
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                s = v + nums[l] + nums[r]
                if s > 0:
                    r-=1
                elif s < 0:
                    l+=1
                else:
                    result.append([v, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l+=1
        
        return result