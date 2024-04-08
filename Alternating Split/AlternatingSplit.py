class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __repr__(self):
        return f"Context(first={self.first}, second={self.second})"

def alternating_split(head):
    if head is None or head.next is None:
        raise Exception

    first = Node(head.data)
    second = Node(head.next.data)
    result = Context(first, second)

    head = head.next
    count = 0
    while head.next is not None:
        head = head.next
        if count % 2 == 0:
            first.next = Node(head.data)
            first = first.next
        else:
            second.next = Node(head.data)
            second = second.next
        count += 1
    return result
