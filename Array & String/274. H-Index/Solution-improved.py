class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        for i in range(len(citations)-1, -1, -1):
            if i <= (len(citations)-1)/2:
                return i+1
