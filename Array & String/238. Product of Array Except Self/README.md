# Intuition
전부 다 곱하고 원소로 나눈다.

# Approach
전부 곱하고 원소로 나누되, 변수 3개를 사용해서 0, 전체 곱, 전체 곱이되 0을 제외한 값을 각각 저장한다.

# Complexity
- Time complexity: $$O(n)$$

- Space complexity: $$O(n)$$

# Code
```python3 []
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cn = nums.count(0)
        if cn > 1:
            return [0] * len(nums)

        answer = []
        a, b = 1, 1
        for n in nums:
            if n: a *= n
            b *= n

        for n in nums:
            if n and cn != 1: answer.append(a//n)
            elif n and cn == 1: answer.append(b)
            else: answer.append(a)

        return answer
```
