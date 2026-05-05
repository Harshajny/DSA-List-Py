class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # 'k' is our slow pointer, starting at the second element
        k = 1 
        
        # 'i' is our fast pointer, scanning the rest of the array
        for i in range(1, len(nums)):
            # We want to check if the current element is different 
            # from the one right before it.
            if nums[i] != nums[i - 1]:
                # If it's unique, we "write" it at position 'k'
                nums[k] = nums[i]
                # Then move 'k' forward
                k += 1
        
        return k