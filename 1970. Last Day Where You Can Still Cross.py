class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = row * col
        parent = list(range(n + 2))
        rank = [0] * (n + 2)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            if rank[pa] < rank[pb]:
                pa, pb = pb, pa
            parent[pb] = pa
            if rank[pa] == rank[pb]:
                rank[pa] += 1

        grid = [[0] * col for _ in range(row)]
        TOP = n
        BOTTOM = n + 1
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for day in range(len(cells) - 1, -1, -1):
            r, c = cells[day]
            r -= 1
            c -= 1
            grid[r][c] = 1
            idx = r * col + c

            if r == 0:
                union(idx, TOP)
            if r == row - 1:
                union(idx, BOTTOM)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    union(idx, nr * col + nc)

            if find(TOP) == find(BOTTOM):
                return day
        return 0
