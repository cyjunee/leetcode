class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        out = 0
        for i in range(len(nums)):
            out ^= (i+1)
            out ^= nums[i]
        
        return out