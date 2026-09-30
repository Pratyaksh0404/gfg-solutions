class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Solution:
    def isSubTree(self, root1, root2):
        def serialize(root, path):
            if not root:
                path.append("N") 
                return
            path.append(f",{root.data},")  
            serialize(root.left, path)
            serialize(root.right, path)

        if not root2:
            return True
        if not root1:
            return False

        s1 = []
        s2 = []
        serialize(root1, s1)
        serialize(root2, s2)

        ss1 = "".join(s1)
        ss2 = "".join(s2)

        return ss2 in ss1