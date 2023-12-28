from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = [], []
        l, r = -1, -1
        length = len(height)
        for index in range(length):
            left.append(l)
            right.append(r)
            if height[index] > l:
                l = height[index]
            if height[length - 1 - index] > r:
                r = height[length - 1 - index]
        right.reverse()
        total = 0
        for index in range(length):
            total += max(min(left[index], right[index])-height[index], 0)
        return total
