from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)

        result = ""

        for ch, freq in sorted(count.items(), key=lambda x: x[1], reverse=True):
            result += ch * freq

        return result