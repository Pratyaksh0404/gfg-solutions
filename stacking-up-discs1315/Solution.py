class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, idx, val):
        while idx <= self.size:
            if val > self.tree[idx]:
                self.tree[idx] = val
            idx += idx & (-idx)

    def query(self, idx):
        max_val = 0
        while idx > 0:
            if self.tree[idx] > max_val:
                max_val = self.tree[idx]
            idx -= idx & (-idx)
        return max_val

class Solution:
    def maxStackHeight(self, r, h):
        discs = sorted(zip(r, h), key=lambda x: (x[0], -x[1]))

        max_h = max(h) if h else 0
        bit = FenwickTree(max_h)

        overall_max_height = 0

        for radius, height in discs:
            prev_max = bit.query(height - 1)
            current_max = prev_max + height
            bit.update(height, current_max)
            if current_max > overall_max_height:
                overall_max_height = current_max

        return overall_max_height