class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        c_counter = [0 for i in range(n+1)]

        for c in citations:
            if c >= n:
                c_counter[n] += 1
            else:
                c_counter[c] += 1
        
        for i in range(n):
            if sum(c_counter[i:]) < i:
                return i-1

        
