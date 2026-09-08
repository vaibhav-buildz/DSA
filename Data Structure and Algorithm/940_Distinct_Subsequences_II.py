class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        total = 0
        end = [0] * 26

        for c in s:
            index = ord(c) - ord('a')

            old_total = total
            new_subsequences = (old_total + 1 - end[index] + MOD) % MOD

            total = (total + new_subsequences) % MOD
            end[index] = (end[index] + new_subsequences) % MOD

        return total