from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merge = []
        intervals.sort(key=lambda x : x[0])
        for start, end in intervals:

            if not merge:
                merge.append([start, end])
            elif merge[-1][1] < start:
                merge.append([start, end])
            else:
                merge[-1][1] = max(merge[-1][1], end)

        return merge