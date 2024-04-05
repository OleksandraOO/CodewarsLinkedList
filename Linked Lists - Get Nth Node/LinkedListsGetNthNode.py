class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    temp = node
    n = 0
    while temp:
        if n == index:
            return temp.data
        n+=1
        temp = temp.next
    raise Exception
