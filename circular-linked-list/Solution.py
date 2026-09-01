#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None

class Solution:
    def isCircular(self, head):
        if head is None:
            return False

        temp = head.next

        while temp is not None and temp != head:
            temp = temp.next

        if temp == head:
            return True
        else:
            return False