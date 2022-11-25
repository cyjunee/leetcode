class Solution:
    def climbStairs(self, n: int) -> int:
        stair = [0 for _ in range(46)]
        stair[1] = 1
        stair[2] = 2
        
        for i in range(3, n+1):
            stair[i] = stair[i-1] + stair[i-2]
        
        return stair[n]