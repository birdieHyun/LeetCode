import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        missing = len(t)
        counter = collections.Counter(t)
        left = start = end = 0
        for right in range(1, len(s) + 1):
            if s[right - 1] in counter:
                missing -= counter[s[right - 1]] > 0
                counter[s[right - 1]] -= 1

            if missing == 0:
                while left < right and (s[left] not in counter or counter[s[left]] < 0):
                    if s[left] in counter:
                        counter[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right

        return s[start:end]
