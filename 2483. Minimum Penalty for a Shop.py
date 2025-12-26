class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count('Y')
        best = penalty
        best_hour = 0
        
        for i, ch in enumerate(customers):
            if ch == 'Y':
                penalty -= 1
            else:
                penalty += 1
            
            if penalty < best:
                best = penalty
                best_hour = i + 1
        
        return best_hour
