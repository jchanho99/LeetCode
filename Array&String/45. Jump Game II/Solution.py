class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        
        i, j, count = 0, nums[0], 0

        while i <= len(nums)-1:
            for ii in range(i+1, i+j+1):
                if ii < len(nums) and ii+nums[ii] > j:
                    j = ii+nums[ii]
                    i = ii
            count += 1
            
        return count 
