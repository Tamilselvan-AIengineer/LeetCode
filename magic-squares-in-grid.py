class Solution:
    def numMagicSquaresInside(self, grid):
        rows, cols = len(grid), len(grid[0])
        ans = 0
        
        def isMagic(r, c):
            nums = []
            for i in range(r, r+3):
                for j in range(c, c+3):
                    nums.append(grid[i][j])
            
            if sorted(nums) != [1,2,3,4,5,6,7,8,9]:
                return False
            
            if grid[r+1][c+1] != 5:
                return False
            
            s = 15
            
            for i in range(3):
                if sum(grid[r+i][c:c+3]) != s:
                    return False
            
            for j in range(3):
                if grid[r][c+j] + grid[r+1][c+j] + grid[r+2][c+j] != s:
                    return False
            
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != s:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != s:
                return False
            
            return True
        
        for r in range(rows-2):
            for c in range(cols-2):
                if isMagic(r, c):
                    ans += 1
        
        return ans
