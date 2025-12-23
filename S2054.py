from bisect import bisect_left

class Solution:
    def maxTwoEvents(self, events):
        # Sort events by end time
        events.sort(key=lambda x: x[1])

        # ends[i] = end time of ith event
        ends = [e[1] for e in events]

        # prefix_max[i] = max value among events[0..i]
        prefix_max = [0] * len(events)
        prefix_max[0] = events[0][2]

        for i in range(1, len(events)):
            prefix_max[i] = max(prefix_max[i - 1], events[i][2])

        ans = 0

        for i, (start, end, value) in enumerate(events):
            # Find last event that ends < start
            idx = bisect_left(ends, start) - 1

            if idx >= 0:
                ans = max(ans, value + prefix_max[idx])

            # Also consider taking this event alone
            ans = max(ans, value)

        return ans
