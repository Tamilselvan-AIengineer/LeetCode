class Solution:
    def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
        # maps: row x -> (min_y, max_y), col y -> (min_x, max_x)
        row_min = {}
        row_max = {}
        col_min = {}
        col_max = {}

        for x, y in buildings:
            if x in row_min:
                row_min[x] = min(row_min[x], y)
                row_max[x] = max(row_max[x], y)
            else:
                row_min[x] = row_max[x] = y

            if y in col_min:
                col_min[y] = min(col_min[y], x)
                col_max[y] = max(col_max[y], x)
            else:
                col_min[y] = col_max[y] = x

        count = 0
        for x, y in buildings:
            if row_min[x] < y < row_max[x] and col_min[y] < x < col_max[y]:
                count += 1

        return count
