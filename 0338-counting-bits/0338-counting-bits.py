class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        out = [0 for i in range(n+1)]
        out[1] = 1
        
        idx = 2
        period = 2
        
        while idx <= n:
            for i in range(period):
                if idx + i > n:
                    break
                out[idx+i] = out[i] + 1
            
            idx += period
            period *= 2
        
        return out