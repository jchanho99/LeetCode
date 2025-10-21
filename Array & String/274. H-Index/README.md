# Intuition
적어도 i개 이상 논문을 내고, i번 이상 인용한, 가장 큰 i를 고른다.

# Approach
논문 개수를 바탕으로 filter를 사용하여 필터링된 논문의 개수가 더 많으면 그 값으로 갱신한다.

# Complexity
- Time complexity: $$O(n^2)$$, sort를 하지 않았다. 아마 sort하면 더 빨라질 것이다.

- Space complexity: $$O(n)$$

# Code
```python3 []
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        answer = 0
        for c in range(1, len(citations)+1):
            if c <= len(list(filter(lambda x: x >= c, citations))) and c > answer:
                answer = c
        return answer
```
