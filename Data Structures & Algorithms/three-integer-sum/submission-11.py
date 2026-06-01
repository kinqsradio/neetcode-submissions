class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 2 pointers
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
                    # Way 1
                    if [v, nums[l], nums[r]] not in result:
                        result.append([v, nums[l], nums[r]])

                    # result.append([v, nums[l], nums[r]])
                    l+=1
                    r-=1
                    # Way 2
                    # while nums[l] == nums[l - 1] and l < r:
                    #     l+=1
        
        return result

        # bruteforce
        # result = []
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in result:
        #                     result.append([nums[i], nums[j], nums[k]])

        # return result