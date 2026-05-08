class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        exp_sum=int((n*(n+1))/2)
        curr_sum=sum(nums)
        return(exp_sum-curr_sum)
