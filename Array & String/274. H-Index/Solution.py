class Solution:
    def hIndex(self, citations: List[int]) -> int:
        answer = 0
        for c in range(1, len(citations)+1):
            if c <= len(list(filter(lambda x: x >= c, citations))) and c > answer:
                answer = c
        return answer
