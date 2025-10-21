# Intuition
최대한 갈 수 있는 장소를 고르고, 또 그곳에서 최대한 갈 수 있는 경로로만 가면 편하다.

# Approach
DFS로 처음엔 가려다가 나중에 for 문으로 최댓값 고르는 식으로 틀었다.
 
# Complexity
- Time complexity:  <= $$O(n)$$, 원소값이 전부 1이 아니지 않은 이상 이것보단 빨리 나올 것이다. 

- Space complexity: $$O(n)$$, Set에 저장해야 하니 이 정도는 든다.

# Code
```python3 []
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        i, j, count = 0, nums[0], 0
        visited = {0}
        
        # 제일 멀리 가는 놈을 뽑고, 그 길로 또 길게 가는 놈을 뽑는다.
        # 맨 마지막에 다다르면 count에 추가
        while len(visited) != len(nums):
            for ii in range(i+1, i+j+1):
                if ii >= len(nums):
                    break

                if ii not in visited and ii+nums[ii] > j:
                    j = ii+nums[ii]
                    i = ii

                visited.add(ii)
            j = nums[i]
            count += 1
        
        return count
```
