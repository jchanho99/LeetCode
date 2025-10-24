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
