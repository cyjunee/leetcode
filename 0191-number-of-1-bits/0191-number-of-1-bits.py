class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 0xffffffff
        n &= mask
        count_one = 0
        
        for i in range(32):
            if n & 1:
                count_one += 1
            n >>= 1
            
        return count_one