from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda num: num[0])
        print(intervals)
        ans = []
        st = intervals[0][0]
        end = intervals[0][1]
        for interval in intervals:
            if interval[0] <= end:
                end = max(interval[1], end)
            else:
                ans.append([st, end])
                st = interval[0]
                end = interval[1]
        if not ans or ans[-1] != [st, end]:
            ans.append([st, end])

        return ans

intervals = [[1,4],[0,4]]
solution = Solution()
solution.merge(intervals)