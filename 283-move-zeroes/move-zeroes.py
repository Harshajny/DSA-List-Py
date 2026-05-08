class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        x=0
        for i in range(len(nums)):
            if nums[i]!=0:
               nums[x], nums[i] = nums[i], nums[x]
               x += 1
                
 
        # x tracks where the next non-zero should be placed
        x = 0
        
        for i in range(len(nums)):
            # If we find a non-zero number
            if nums[i] != 0:
                # Swap it with the element at position x
                nums[x], nums[i] = nums[i], nums[x]
                
                # Increment x to the next available spot
                x += 1
        