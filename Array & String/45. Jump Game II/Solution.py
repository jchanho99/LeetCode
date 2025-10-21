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
