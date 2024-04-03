class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def push(head, data):
    new = Node(data)
    if not head:
        return new
    new.next = head
    return new

def build_one_two_three():
    head = None
    for i in [3,2,1]:
        head = push(head, i)
    return head
