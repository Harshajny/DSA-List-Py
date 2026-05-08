class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_val=0
        current=0
        for i in nums:
            if(i==1):
                current=current+1
                if current>=max_val:
                    max_val=current

            else:
                current=0
        

        return max_val
        