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
