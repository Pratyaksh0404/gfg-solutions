import bisect


class Solution:

  def findKthSmall(self, arr, k):
    arr.sort()
    low, high = 1, k + len(arr)
    ans = high
    while low <= high:
      mid = (low + high) // 2
      c = bisect.bisect_right(arr, mid)
      if mid - c >= k:
        ans = mid
        high = mid - 1
      else:
        low = mid + 1
    return ans