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
