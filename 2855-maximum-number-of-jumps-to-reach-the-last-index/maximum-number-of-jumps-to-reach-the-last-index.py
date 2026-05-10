class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # dp[i] will store the max jumps to reach index i
        dp = [-1] * n
        dp[0] = 0
        
        # We iterate through each possible landing spot 'j'
        for j in range(1, n):
            # For each 'j', we check all possible previous spots 'i'
            for i in range(j):
                # Check if i was reachable and if the jump to j is valid
                if dp[i] != -1 and -target <= nums[j] - nums[i] <= target:
                    # We want the maximum jumps, so we take the best path found so far
                    dp[j] = max(dp[j], dp[i] + 1)
        
        return dp[n-1]