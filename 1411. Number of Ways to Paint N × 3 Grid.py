class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        same = 6   # ABA type
        diff = 6   # ABC type
        
        for _ in range(2, n + 1):
            newSame = (same * 3 + diff * 2) % MOD
            newDiff = (same * 2 + diff * 2) % MOD
            
            same, diff = newSame, newDiff
        
        return (same + diff) % MOD
