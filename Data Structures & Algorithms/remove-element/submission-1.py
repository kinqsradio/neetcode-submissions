class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # BruteForce
        # temp = []
        # for num in nums:
        #     if num == val:
        #         continue
        #     temp.append(num)
        # for i in range(len(temp)):
        #     nums[i] = temp[i]
        
        # return len(temp)

        # 2 Pointer
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k