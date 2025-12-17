from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        INF = 10**18

        # dp[t][0] = flat (no position)
        # dp[t][1] = holding long
        # dp[t][2] = holding short
        dp = [[-INF] * 3 for _ in range(k + 1)]
        dp[0][0] = 0

        for price in prices:
            new_dp = [row[:] for row in dp]

            for t in range(k + 1):
                # Start a long position (buy)
                new_dp[t][1] = max(new_dp[t][1], dp[t][0] - price)

                # Start a short position (sell)
                new_dp[t][2] = max(new_dp[t][2], dp[t][0] + price)

                if t + 1 <= k:
                    # Close long (sell)
                    new_dp[t + 1][0] = max(new_dp[t + 1][0], dp[t][1] + price)

                    # Close short (buy back)
                    new_dp[t + 1][0] = max(new_dp[t + 1][0], dp[t][2] - price)

            dp = new_dp

        return max(dp[t][0] for t in range(k + 1))
