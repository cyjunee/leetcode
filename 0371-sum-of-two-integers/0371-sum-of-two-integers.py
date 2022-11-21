class Solution:
    def full_adder(self, a: int, b: int, c_in: int) -> (int, int):
        s = a ^ b ^ c_in
        c_out = ((a ^ b) & c_in) | (a & b) 
        return (s, c_out)

    def getSum(self, a: int, b: int) -> int:
        result = 0
        carry = 0
        mask = 0xffffffff

        for i in range(32):
            s, carry = self.full_adder(a & 1, b & 1, carry)
            result ^= (s << i)
            a >>= 1
            b >>= 1

        if (result >> 31) == 1:
            return ~(mask ^ result)
            
        return result