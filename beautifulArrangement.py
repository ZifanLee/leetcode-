class Solution:
    def countArrangement(self, n: int) -> int:
        occupied = [False for i in range(n + 1)]
        nums = [i for i in range(1, n + 1)]
        res = 0

        def dfs(st):
            nonlocal occupied, nums
            nonlocal res
            if st == n:
                res += 1
                return
            for num in nums:
                if not occupied[num] and (num % (st + 1) == 0 or (st + 1) % num == 0):
                    occupied[num] = True
                    dfs(st + 1)
                    occupied[num] = False

        dfs(0)
        return res
