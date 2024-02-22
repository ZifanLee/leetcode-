from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = [0]*(len(nums1)+len(nums2))
        if len(nums)%2 == 0:
            t1, t2 = len(nums)//2 - 1, len(nums)//2
        else:
            t1, t2 = len(nums)//2, len(nums)//2
        i, j, ptr = 0, 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums[ptr] = nums1[i]
                ptr += 1
                i += 1
            else:
                nums[ptr] = nums2[j]
                ptr += 1
                j += 1
            if ptr > t2:
                return (nums[t1]+nums[t2])/2
        while i < len(nums1):
            nums[ptr] = nums1[i]
            ptr += 1
            i += 1
            if ptr > t2:
                return (nums[t1]+nums[t2])/2
        while j < len(nums2):
            nums[ptr] = nums2[j]
            ptr += 1
            j += 1
            if ptr > t2:
                return (nums[t1]+nums[t2])/2
        return (nums[t1]+nums[t2])/2


nums1 = [2,3]
nums2 = []
solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))