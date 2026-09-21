"""
Structure of binary tree Node
class Node:
    def __init__(self, x: int):
        self.data = x
        self.left = self.right = None
"""


from collections import deque

class Solution:

    def areAnagrams(self, root1, root2) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        q1, q2 = deque([root1]), deque([root2])

        while q1 and q2:
            if len(q1) != len(q2):
                return False

            level1, level2 = [], []

            for _ in range(len(q1)):
                node1, node2 = q1.popleft(), q2.popleft()

                level1.append(node1.data)
                level2.append(node2.data)

                for n in (node1.left, node1.right):
                    if n:
                        q1.append(n)
                for n in (node2.left, node2.right):
                    if n:
                        q2.append(n)

            if sorted(level1) != sorted(level2):
                return False

        return not q1 and not q2