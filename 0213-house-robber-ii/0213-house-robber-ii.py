from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 3:
            return max(nums)
        
        first = nums[:-1]
        second = nums[1:]

        dp_1 = [0] * (len(first) + 1)
        dp_2 = [0] * (len(second) + 1)

        dp_1[1] = first[0]
        dp_2[1] = second[0]

        for i in range(1, len(first) + 1):
            dp_1[i] = max(dp_1[i - 1], dp_1[i - 2] + first[i - 1])
            dp_2[i] = max(dp_2[i - 1], dp_2[i - 2] + second[i - 1])

        return max(dp_1[-1], dp_2[-1])

