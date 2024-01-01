from collections import deque
from typing import List


def quickSort(nums: List[int]) -> List[int]:
    if not nums or len(nums) == 1:
        return nums
    low,eql, high = [], [nums[0]], []
    cardinality = nums[0]
    for index in range(1, len(nums)):
        if nums[index] < cardinality:
            low.append(nums[index])
        elif nums[index] == cardinality:
            eql.append(nums[index])
        else:
            high.append(nums[index])
    return quickSort(low) + eql + quickSort(high)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        cardinality = nums[0]
        low, eql, high = [], [nums[0]], []
        for index in range(1, len(nums)):
            if nums[index] < cardinality:
                low.append(nums[index])
            elif nums[index] == cardinality:
                eql.append(nums[index])
            else:
                high.append(nums[index])
        if len(high) == k-1:
            return cardinality
        elif len(high) < k-1:
            if len(eql) + len(high) >= k:
                return cardinality
            else:
                return self.findKthLargest(low, k-len(high)-len(eql))
        else:
            return self.findKthLargest(high, k)

solution =Solution()
print(solution.findKthLargest([-1, -1], 2))
