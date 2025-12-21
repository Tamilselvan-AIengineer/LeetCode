class Solution:
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])
        
        sorted_pairs = [False] * (n - 1)
        deletions = 0
        
        for col in range(m):
            bad = False
            
            # Check if this column breaks ordering
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][col] > strs[i + 1][col]:
                    bad = True
                    break
            
            if bad:
                deletions += 1
                continue
            
            # Update sorted_pairs
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][col] < strs[i + 1][col]:
                    sorted_pairs[i] = True
            
            # Optimization: if all pairs sorted, stop early
            if all(sorted_pairs):
                break
        
        return deletions
