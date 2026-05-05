class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i,n in enumerate(nums): #just asks for the next time
            diff=target-n
            if diff in dict:
                return[dict[diff],i]
            dict[n]=i #assigning value to key
        return []