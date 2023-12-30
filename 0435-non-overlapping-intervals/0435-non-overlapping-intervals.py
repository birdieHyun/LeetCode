from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        answer = 0

        prev_end = intervals[0][1]

        for i in intervals[1:]:
            start, end = i[0], i[1]

            if start >= prev_end:
                prev_end = end
            else:
                answer += 1
                prev_end = min(end, prev_end)

        return answer
