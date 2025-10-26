class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # set()을 사용하면 공간을 포기하고, for를 사용하면 시간을 포기하고..
        
        
        # nums.sort()
        # i, k, d = 0, len(nums)-1, True
        # answer = set()

        # while (k-i) >= 2:
        #     temp = nums[i]+nums[k]
        #     if -temp in set(nums[i+1:k]):
        #         answer.add((nums[i], -temp, nums[k]))

        #     if d: 
        #         i += 1
        #         d = False
        #     else: 
        #         k -= 1
        #         d = True

        # return [list(i) for i in answer]


        nums.sort()  # Sort the array to enable two-pointer technique and handle duplicates easily
        n = len(nums)
        answer = []

        for i in range(n - 2):
            # Skip duplicate values for the first element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # If the current element is positive, no further triplets can sum to zero
            # as all subsequent elements will also be positive
            if nums[i] > 0:
                break

            j, k = i + 1, n - 1  # Initialize two pointers

            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]

                if current_sum == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    # Skip duplicate values for left and right pointers
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif current_sum < 0:
                    j += 1  # Increase sum by moving left pointer to a larger value
                else:  # current_sum > 0
                    k -= 1  # Decrease sum by moving right pointer to a smaller value
        return answer
