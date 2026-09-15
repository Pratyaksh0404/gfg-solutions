''' Binary Tree Node Structure
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getCount(self, root, k):
        leaves = []
        def dfs(node, level):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(level)
                return
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 1)
        leaves.sort()

        count = 0
        for cost in leaves:
            if k >= cost:
                k -= cost
                count += 1
            else:
                break
        return count