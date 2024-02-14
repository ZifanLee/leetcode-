from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totalSum = 0
        for item in nums:
            totalSum += item
        if totalSum % k != 0:
            return False
        target = totalSum / k
        jumps = []
        for index, item in enumerate(nums):
            if item > target:
                return False
            if item == target:
                jumps.append(index)

        nums = [item for index, item in enumerate(nums) if index not in jumps]
        k -= len(jumps)
        occupied = [False]*len(nums)

        def dfs(st, current, k):
            nonlocal nums,occupied
            if k == 0:
                return True
            if st > len(nums):
                return False
            if current < 0:
                return False
            if current == 0:
                if dfs(0, target, k - 1):
                    return True
                return False

            for index in range(st, len(nums)):
                if occupied[index]:
                    continue
                item = nums[index]
                occupied[index] = True
                if dfs(index+1, current - item, k):
                    return True
                occupied[index] = False
            return False

        return dfs(0, target, k)

solution = Solution()
print(solution.canPartitionKSubsets(nums=[815,625,3889,4471,60,494,944,1118,4623,497,771,679,1240,202,601,883], k=3))