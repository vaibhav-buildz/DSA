class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        pref = [0] * n
        timer = 0

        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1
                pref[u] = (pref[p] if p != -1 else 0) ^ (1 << (ord(s[u]) - 97))
                parent[0][u] = u if p == -1 else p

                stack.append((u, p, 1))
                for v in reversed(g[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        for j in range(1, LOG):
            for u in range(n):
                parent[j][u] = parent[j - 1][parent[j - 1][u]]

        bit = [0] * (n + 2)

        def add(i, val):
            while i <= n + 1:
                bit[i] ^= val
                i += i & -i

        def get(i):
            val = 0
            while i:
                val ^= bit[i]
                i -= i & -i
            return val

        def update_range(l, r, val):
            add(l + 1, val)
            add(r + 2, val)

        def prefix(u):
            return pref[u] ^ get(tin[u] + 1)

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            d = depth[u] - depth[v]
            j = 0
            while d:
                if d & 1:
                    u = parent[j][u]
                d >>= 1
                j += 1

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if parent[j][u] != parent[j][v]:
                    u = parent[j][u]
                    v = parent[j][v]

            return parent[0][u]

        chars = [1 << (ord(c) - 97) for c in s]
        ans = []

        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = 1 << (ord(parts[2]) - 97)

                if chars[u] != c:
                    update_range(tin[u], tout[u], chars[u] ^ c)
                    chars[u] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)
                mask = prefix(u) ^ prefix(v) ^ chars[w]
                ans.append((mask & (mask - 1)) == 0)

        return ans