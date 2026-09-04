class Solution:
    def majorityElement(self, arr):
        c = 0
        a = None
        for num in arr:
            if c == 0:
                a = num
                c = 1
            elif num == a:
                c += 1
            else:
                c -= 1

        if arr.count(a) > len(arr) // 2:
            return a
        else:
            return -1