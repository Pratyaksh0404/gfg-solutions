class Solution:
    def profession(self, level, pos):
        return "Doctor" if (pos - 1).bit_count() % 2 else "Engineer"
