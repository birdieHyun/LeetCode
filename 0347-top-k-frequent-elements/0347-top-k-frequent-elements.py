import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        q = []
        answer = []
        nums_set = set(nums)

        for i in nums_set:
            heapq.heappush(q, (-nums.count(i), i))

        for i in range(k):
            answer.append(heapq.heappop(q)[1])

        return answer