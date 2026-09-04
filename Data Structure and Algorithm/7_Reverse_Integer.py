class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1

        num = abs(x)
        reversed_str = str(num)[::-1]
        val = sign * int(reversed_str)

        if val < -2**31 or val > 2**31 - 1:
            return 0
        else:
            return val