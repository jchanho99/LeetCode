# Intuition
left, right 포인터를 설정해서 왔다갔다 한다.

# Approach
`nums[left] + nums[right]` 값을 기준으로, (1) 작거나 (2) 크거나 (3) 맞는 경우로 나눠서 연산한다.

# Complexity
- Time complexity: $$O(n)$$, `numbers` array만큼 연산한다.

- Space complexity: $$O(n)$$, 변수 1개만 사용했으니 정확하게는 $$O(n)+O(1)$$이다.

# Code
```python3 []
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1

        while left != right:
            temp = numbers[left] + numbers[right]
            if temp == target:
                return [left+1, right+1]
            elif temp < target:
                left += 1
            else:
                right -= 1
```
