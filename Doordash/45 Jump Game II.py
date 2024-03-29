### Greedy Algorithm
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Greedy algorithm
        # For each phase, select the step that can take you to the farthest point
        farthest = 0
        current_end = 0
        jump_step = 0
        
        # Iteration
        for i in range(len(nums) - 1):
            # Update the farthest point
            farthest = max(i + nums[i], farthest)
            # When we reach the end of the current phase, need to jump another step
            if i == current_end:
                jump_step += 1
                current_end = farthest
        
        return jump_step

 

### DP
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Dynamic Programming
        # Initialization
        dp = [float("inf") for i in range(len(nums))]
        dp[0] = 0
        
        # Iterate through each point in the nums array
        for i in range(len(nums)):
            max_step = nums[i]
            for j in range(1, max_step + 1, 1):
                if (i + j) >= len(nums):
                    break
                dp[i + j] = min(dp[i + j], dp[i] + 1)
        
        # return
        return dp[len(nums) - 1]
