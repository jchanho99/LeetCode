# Intuition
투 포인터를 사용한다.

# Approach
양 끝단(왼쪽, 오른쪽)에서 시작해서 작은 높이를 가진 포인터에 기준을 맞추고, 해당 포인터를 다시 한 칸 움직인다.
계산한 넓이가 전에 계산했던 넓이보다 넓다면 갱신한다.

# Complexity
- Time complexity: $$O(n)$$, `38ms, 95.79% 백분위`

- Space complexity: $$O(n)$$, `28.51MB, 24.02% 백분위`

# Code
```python3 []
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        answer = 0

        while left != right:
            h = 0
            if height[left] >= height[right]:
                h = height[right]*(right-left)
                right -= 1
            else:
                h = height[left]*(right-left)
                left += 1
                
            answer = h if h > answer else answer

        return answer
```
