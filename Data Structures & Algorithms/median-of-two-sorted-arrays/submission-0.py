class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined_list = nums1 + nums2
        combined_list.sort()

        total_length = len(combined_list)
        if total_length % 2 == 0:
            return (combined_list[total_length // 2 -1] + combined_list[total_length // 2]) / 2
        else:
            return combined_list[total_length//2]
        return 1
        