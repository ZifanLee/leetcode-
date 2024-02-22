class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0

        def binary_search(l, r):
            nonlocal x
            nonlocal ans
            mid = (l+r)//2
            if l > r:
                return
            if mid*mid == x:
                ans = mid
                return
            elif mid*mid > x:
                binary_search(l, mid-1)
            else:
                ans = mid
                binary_search(mid+1, r)

        binary_search(1, x)
        return ans

solution = Solution()
print(solution.mySqrt(10))