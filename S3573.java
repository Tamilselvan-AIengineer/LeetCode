import java.util.*;

class Solution {
    public long maximumProfit(int[] prices, int k) {
        long NEG = Long.MIN_VALUE / 4;

        // dp[t][0] = flat
        // dp[t][1] = holding long
        // dp[t][2] = holding short
        long[][] dp = new long[k + 1][3];
        for (int t = 0; t <= k; t++) {
            Arrays.fill(dp[t], NEG);
        }
        dp[0][0] = 0;

        for (int price : prices) {
            long[][] next = new long[k + 1][3];
            for (int t = 0; t <= k; t++) {
                Arrays.fill(next[t], NEG);
            }

            for (int t = 0; t <= k; t++) {
                // stay in same state
                for (int s = 0; s < 3; s++) {
                    next[t][s] = Math.max(next[t][s], dp[t][s]);
                }

                // start long
                next[t][1] = Math.max(next[t][1], dp[t][0] - price);

                // start short
                next[t][2] = Math.max(next[t][2], dp[t][0] + price);

                if (t + 1 <= k) {
                    // close long
                    next[t + 1][0] = Math.max(next[t + 1][0], dp[t][1] + price);
                    // close short
                    next[t + 1][0] = Math.max(next[t + 1][0], dp[t][2] - price);
                }
            }

            dp = next;
        }

        long ans = 0;
        for (int t = 0; t <= k; t++) {
            ans = Math.max(ans, dp[t][0]);
        }
        return ans;
    }
}
