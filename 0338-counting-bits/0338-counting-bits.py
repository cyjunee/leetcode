class Solution:
    def countBits(self, n: int) -> List[int]:
        out = [0]
        
        for i in range(1,n+1):
            out.append(i % 2 + out[i>>1])
            
        return out