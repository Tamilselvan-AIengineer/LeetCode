class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        total_apples = sum(apple)
        
        capacity.sort(reverse=True)
        
        used_capacity = 0
        boxes = 0
        
        for cap in capacity:
            used_capacity += cap
            boxes += 1
            if used_capacity >= total_apples:
                return boxes
