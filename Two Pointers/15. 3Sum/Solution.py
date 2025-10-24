class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # set()을 사용하면 공간을 포기하고, for를 사용하면 시간을 포기하고..
        i, k, d = 0, len(nums)-1, True
        answer = []
        
        while i < k:
            temp = nums[i]+nums[k]
            if -temp in set(nums[i+1:k]):
                answer.append([nums[i], -temp, nums[k]])
            
            if d:
                i += 1
                d = False
            else:
                k -= 1
                d = True

        return answer
