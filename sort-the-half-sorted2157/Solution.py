class Solution:
    def mergeTwoParts(self, arr):
        n = len(arr)
        index = 0

        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                index = i + 1
                break

        if index == 0:
            return

        temp = [0] * n
        i = 0
        j = index
        k = 0

        while i < index and j < n:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1

        while i < index:
            temp[k] = arr[i]
            i += 1
            k += 1

        while j < n:
            temp[k] = arr[j]
            j += 1
            k += 1

        for x in range(n):
            arr[x] = temp[x]