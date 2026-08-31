class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        val = sign * int(str(abs(x))[::-1])
        return val if -2**31 <= val <= 2**31 - 1 else 0