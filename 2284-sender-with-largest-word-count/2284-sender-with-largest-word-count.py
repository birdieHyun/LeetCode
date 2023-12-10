from typing import List
from collections import defaultdict
import heapq

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:

        dicts = defaultdict(int)
        q = []

        for i in range(len(senders)):
            sender = senders[i]
            message = len(messages[i].split())
            dicts[sender] += message

        sender_set = set(senders)

        for i in sender_set:
            heapq.heappush(q, (dicts[i], i))

        return heapq.nlargest(1, q)[0][1]  # nlargest를 사용하여 가장 큰 요소 반환