class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        n=len(nums)
        esum=0
        dsum=0
        for i in range(n):
            esum=esum+nums[i]
            digits = [int(d) for d in str(nums[i])]
            for j in range(len(digits)):
                dsum=dsum+digits[j]
        return(abs(esum-dsum))
        