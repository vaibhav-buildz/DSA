#1st
class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        for a in range(1, n+1):
            if a > 999:
                res += 1
        return res



#2nd
class Solution:
    def countCommas(self, n: int) -> int:
        return max(n - 999, 0)