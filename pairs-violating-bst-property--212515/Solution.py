class Solution:
    def pairsViolatingBST(self, root):
        def merge_sort(arr, temp, left, right):
            inv_count = 0
            if left < right:
                mid = (left + right) // 2
                inv_count += merge_sort(arr, temp, left, mid)
                inv_count += merge_sort(arr, temp, mid + 1, right)
                inv_count += merge(arr, temp, left, mid, right)
            return inv_count

        def merge(arr, temp, left, mid, right):
            i = left
            j = mid + 1
            k = left
            inv_count = 0

            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    inv_count += (mid - i + 1)
                    j += 1
                k += 1

            while i <= mid:
                temp[k] = arr[i]
                i += 1
                k += 1

            while j <= right:
                temp[k] = arr[j]
                j += 1
                k += 1

            for i in range(left, right + 1):
                arr[i] = temp[i]

            return inv_count

        inorder = []
        def get_inorder(node):
            if not node:
                return
            get_inorder(node.left)
            inorder.append(node.data)
            get_inorder(node.right)

        get_inorder(root)
        n = len(inorder)
        temp = [0] * n
        return merge_sort(inorder, temp, 0, n - 1)