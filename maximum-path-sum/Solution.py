'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''

class Solution:
    def maxPathSum(self, root):
        self.res = -float('inf')

        def dfs(node):
            if not node:
                return -float('inf')
            if not node.left and not node.right:
                return node.data

            l = dfs(node.left)
            r = dfs(node.right)

            if node.left and node.right:
                self.res = max(self.res, l + r + node.data)
                return node.data + max(l, r)

            if node.left:
                return node.data + l
            return node.data + r

        dfs(root)

        return self.res if self.res != -float('inf') else -1