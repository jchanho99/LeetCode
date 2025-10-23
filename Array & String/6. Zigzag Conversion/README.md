# Intuition
반복이 보인다..!


# Approach
- 일자로 들어가는 부분과 주루룩 올라가는 부분을 나눠봤다.
- 포인터 방식으로, 문자열 길이가 넘으면 종료하는 식으로 한다.


# Complexity
- Time complexity: $$O(n)$$

- Space complexity: $$O(n)$$

# Code
```python3 []
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows: return s

        zz = [[] for _ in range(numRows)]
        
        s_pt = 0
        answer = ""
        while s_pt < len(s):
            for i in range(numRows):
                if s_pt == len(s):
                    break
                    
                zz[i].append(s[s_pt])
                s_pt += 1
                
            for i in range(numRows-2, 0, -1):
                if s_pt == len(s):
                    break
                    
                zz[i].append(s[s_pt])
                s_pt += 1

        for i in range(numRows):
            answer += "".join(zz[i])
        
        return answer
                
# 처음에 일자 줄을 완성하고 numRows-1씩 뛴 자리에 numRows-2번 넣고, numRows-1 다음에 일자 줄
```
