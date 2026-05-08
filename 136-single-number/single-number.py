class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for number in nums:
            # The XOR operator '^' cancels out pairs
            result ^= number
        return result