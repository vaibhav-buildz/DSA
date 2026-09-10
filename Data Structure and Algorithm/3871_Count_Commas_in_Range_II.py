class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        threshold = 1000

        while threshold <= n:
            total = total + (n - threshold + 1)
            threshold = threshold * 1000

        return total