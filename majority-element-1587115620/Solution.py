class Solution:
    def majorityElement(self, arr):
        count = 0
        a = None
        for num in arr:
            if count == 0:
                a = num
                count = 1
            elif num == a:
                count += 1
            else:
                count -= 1

        if arr.count(a) > len(arr) // 2:
            return a
        else:
            return -1