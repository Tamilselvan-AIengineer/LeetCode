class Solution:
    def maxDotProduct(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        NEG_INF = -10**9
        
        dp = [[NEG_INF]*(m+1) for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                take = nums1[i]*nums2[j]
                if i+1 < n and j+1 < m:
                    take += max(0, dp[i+1][j+1])
                
                dp[i][j] = max(take, dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]
