class Solution:
    def check(self, nums: List[int]) -> bool:
        #first check if the array is ascending
        x=0 
        for i in range(len(nums)):
           if nums[i]>nums[(i+1) % len(nums)]:
            x=x+1
        if(x<=1):
            return True
        else:
            return False
      

      
