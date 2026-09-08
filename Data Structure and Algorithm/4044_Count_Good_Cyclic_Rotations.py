class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        half = n // 2
        total = sum(nums)
        doubled = nums + nums
        
        window_sum = sum(doubled[0:half])
        count = 0

        for p in range(n):
            if 2 * window_sum > total:
                count += 1
            window_sum += doubled[p + half] - doubled[p]

        return count