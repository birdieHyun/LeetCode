class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dicts = defaultdict(int)

        for i in nums:
            dicts[i] += 1

        nums_set = set(nums)

        answer_list = []

        for i in nums_set:
            answer_list.append((i, dicts[i]))

        answer_list.sort(reverse=True, key= lambda x : x[1])

        answer = []
        print(answer_list)
        for i in range(k):
            answer.append(answer_list[i][0])

        return answer