import heapq
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

        # dist[i][j][d][t] = min cost to reach (i,j) having arrived via direction d, using t turns so far
        # d = 4 means "no direction yet" (start)
        INF = float('inf')
        dist = [[[[INF] * (k + 1) for _ in range(5)] for _ in range(n)] for _ in range(m)]

        start_cost = grid[0][0]
        dist[0][0][4][0] = start_cost
        heap = [(start_cost, 0, 0, 4, 0)]

        target = (m - 1, n - 1)

        while heap:
            cost, i, j, d, t = heapq.heappop(heap)

            if (i, j) == target:
                return cost

            if cost > dist[i][j][d][t]:
                continue

            for idx, (dr, dc) in enumerate(dirs):
                ni, nj = i + dr, j + dc
                if 0 <= ni < m and 0 <= nj < n:
                    if d == 4:
                        nt = t          # first move, no turn
                    elif idx == d:
                        nt = t          # same direction, no turn
                    else:
                        nt = t + 1      # direction changed, turn used

                    if nt > k:
                        continue

                    new_cost = cost + grid[ni][nj]
                    if new_cost < dist[ni][nj][idx][nt]:
                        dist[ni][nj][idx][nt] = new_cost
                        heapq.heappush(heap, (new_cost, ni, nj, idx, nt))

        return -1