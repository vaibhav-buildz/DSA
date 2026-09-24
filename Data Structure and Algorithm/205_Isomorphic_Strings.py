class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        used = set()

        for a, b in zip(s, t):
            if a in mapping and mapping[a] != b:
                return False

            if a not in mapping and b in used:
                return False

            mapping[a] = b
            used.add(b)

        return True