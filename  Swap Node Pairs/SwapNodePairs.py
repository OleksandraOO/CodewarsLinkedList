class Node:
    def __init__(self, next=None):
        self.next = next

    def __repr__(self):
        return f"Node(next={self.next})"

def swap_pairs(head):
    temp = Node()
    temp.next = head
    copy = temp

    while copy.next is not None and copy.next.next is not None:
        first = copy.next
        second = copy.next.next

        copy.next = second
        first.next = second.next
        second.next = first

        copy = copy.next.next
    return temp.next
