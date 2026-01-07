class Solution:
    MOD = 10**9 + 7

    def maxProduct(self, root):
        subtree_sums = []

        def total_sum(node):
            if not node:
                return 0
            s = node.val + total_sum(node.left) + total_sum(node.right)
            subtree_sums.append(s)
            return s

        total = total_sum(root)
        best = 0

        for s in subtree_sums:
            best = max(best, s * (total - s))

        return best % self.MOD
