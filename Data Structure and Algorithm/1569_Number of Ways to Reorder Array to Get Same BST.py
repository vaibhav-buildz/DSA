class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        c = [[1] * (n + 1) for _ in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, i):
                c[i][j] = (c[i-1][j-1] + c[i-1][j]) % MOD

        def dfs(a):
            if len(a) < 3:
                return 1
            left = [x for x in a if x < a[0]]
            right = [x for x in a if x > a[0]]
            return c[len(a)-1][len(left)] * dfs(left) * dfs(right) % MOD

        return (dfs(nums) - 1) % MOD