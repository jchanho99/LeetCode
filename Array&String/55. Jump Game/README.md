# Intuition
모든 길을 다 방문해서 끝까지 갈 수 있는 방법을 찾는다.

# Approach
DFS나 BFS를 활용한다.

# Complexity
- Time complexity: $$O(V+E)$$

- Space complexity: $$O(n)$$

# Code
```python3 []
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        stack = [(0, nums[0])]
        visited = {(0, nums[0])}
        answer = False

        while stack:
            if answer:
                break

            
            i, v = stack.pop()

            if not v and i != len(nums)-1: continue

            for j in range(i, i+v+1):
                if j == len(nums)-1:
                    answer = True
                    break
                
                if (j, nums[j]) not in visited:
                    stack.append((j, nums[j]))
                    visited.add((j, nums[j]))
                
        
        return answer
```
