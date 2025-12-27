import heapq

class Solution:
    def mostBooked(self, n, meetings):
        meetings.sort()

        available = [i for i in range(n)]          # min-heap of free rooms
        heapq.heapify(available)

        busy = []                                   # min-heap of (endTime, room)
        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # free up rooms that are done by 'start'
            while busy and busy[0][0] <= start:
                finish, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
                count[room] += 1
            else:
                finish, room = heapq.heappop(busy)
                newEnd = finish + duration
                heapq.heappush(busy, (newEnd, room))
                count[room] += 1

        # room with max meetings (smallest index on tie)
        ans = 0
        for i in range(1, n):
            if count[i] > count[ans]:
                ans = i
        return ans
