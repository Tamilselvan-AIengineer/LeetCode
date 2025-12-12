class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        from collections import defaultdict
        
        # Group events by timestamp
        grouped = defaultdict(lambda: {"OFFLINE": [], "MESSAGE": []})
        for typ, ts_str, arg in events:
            ts = int(ts_str)
            grouped[ts][typ].append(arg)

        offline_until = [0] * numberOfUsers
        mentions = [0] * numberOfUsers

        # Process timestamps in sorted order
        for ts in sorted(grouped.keys()):

            # 1️⃣ Process OFFLINE events first
            for arg in grouped[ts]["OFFLINE"]:
                uid = int(arg)
                offline_until[uid] = ts + 60

            # 2️⃣ Process MESSAGE events
            for msg in grouped[ts]["MESSAGE"]:
                if msg == "ALL":
                    # All users are mentioned (including offline)
                    for u in range(numberOfUsers):
                        mentions[u] += 1

                elif msg == "HERE":
                    # Only online users are mentioned
                    for u in range(numberOfUsers):
                        if offline_until[u] <= ts:
                            mentions[u] += 1

                else:
                    # id<number> tokens with duplicates allowed
                    for tok in msg.split():
                        if tok.startswith("id"):
                            uid = int(tok[2:])
                            mentions[uid] += 1

        return mentions
