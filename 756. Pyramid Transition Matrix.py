class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = {}
        for s in allowed:
            mp.setdefault(s[:2], []).append(s[2])

        memo = {}

        def dfs(row):
            if len(row) == 1:
                return True
            if row in memo:
                return memo[row]

            def build(i, cur):
                if i == len(row) - 1:
                    return dfs(cur)
                pair = row[i:i+2]
                if pair not in mp:
                    return False
                for c in mp[pair]:
                    if build(i+1, cur + c):
                        return True
                return False

            memo[row] = build(0, "")
            return memo[row]

        return dfs(bottom)
