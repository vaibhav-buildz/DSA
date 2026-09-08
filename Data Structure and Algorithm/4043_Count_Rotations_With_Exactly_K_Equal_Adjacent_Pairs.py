class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        count = 0

        for p in range(n):
            rotation = s[p:] + s[:p]
            score = 0
            for i in range(n - 1):
                if rotation[i] == rotation[i + 1]:
                    score += 1
            if score == k:
                count += 1

        return count