class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x=1
        for i in range(len(nums)-1):
            if(nums[i]!=nums[i+1]):
                nums[x]=nums[i+1]
                x=x+1
                
        return x

#no need of sets as they have said its inplace and sorted, we could use 2 pointers
                      
       