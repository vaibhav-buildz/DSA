
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int],
                         k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if k >= sum(diff):
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2
            need = sum(max(x - mid, 0) for x in diff)

            if need <= k:
                right = mid
            else:
                left = mid + 1

        level = left
        need = sum(max(x - level, 0) for x in diff)
        ans = sum(min(x, level) ** 2 for x in diff)

        return ans - (k - need) * (2 * level - 1)
