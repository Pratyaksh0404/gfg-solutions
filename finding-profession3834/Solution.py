class Solution:
    def profession(self, lev, pos):
        return "Doctor" if (pos - 1).bit_count() % 2 else "Engineer"
