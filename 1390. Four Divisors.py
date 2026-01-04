class Solution:
    def sumFourDivisors(self, nums):
        ans = 0
        
        for n in nums:
            div_sum = 0
            count = 0
            
            d = 1
            while d * d <= n:
                if n % d == 0:
                    other = n // d
                    count += 1
                    div_sum += d
                    
                    if other != d:
                        count += 1
                        div_sum += other
                        
                    if count > 4:
                        break
                d += 1
            
            if count == 4:
                ans += div_sum
        
        return ans
