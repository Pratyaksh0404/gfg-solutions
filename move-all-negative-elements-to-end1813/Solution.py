class Solution:
    def segregateElements(self, arr):
        temp = [x for x in arr if x >= 0]
        temp += [x for x in arr if x < 0]
        arr[:] = temp