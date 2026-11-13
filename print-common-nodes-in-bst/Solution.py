''' 
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findCommon(self, r1: 'Node', r2: 'Node') -> list[int]:
        s1, s2 = [], []
        res = []
        curr1, curr2 = r1, r2

        while (curr1 or s1) and (curr2 or s2):
            while curr1:
                s1.append(curr1)
                curr1 = curr1.left
            while curr2:
                s2.append(curr2)
                curr2 = curr2.left

            curr1 = s1[-1]
            curr2 = s2[-1]

            if curr1.data == curr2.data:
                res.append(curr1.data)
                s1.pop()
                s2.pop()
                curr1 = curr1.right
                curr2 = curr2.right
            elif curr1.data < curr2.data:
                s1.pop()
                curr1 = curr1.right
                curr2 = None
            else:
                s2.pop()
                curr2 = curr2.right
                curr1 = None

        return res