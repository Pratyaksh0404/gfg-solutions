'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
class Solution:
    def leftView(self, root):
        if not root:
            return []

        ans = []
        queue = [root]

        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if i == 0:
                    ans.append(node.data)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return ans
