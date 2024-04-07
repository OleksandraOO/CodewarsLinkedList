class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f'({self.data}, {self.next})'

def reverse(head):
    if head is None or head.next is None:
        return head

    temp = reverse(head.next)
    next_next = head.next.next
    next_ = head.next
    head.next.next = head
    next_next = head
    head.next = None

    return temp


def stringify(node: Node):
    if node is None:
        return "None"
    else:
        return str(node.data) + " -> " + stringify(node.next)

# lst = Node(1)
# lst.next = Node(2)
# lst.next.next = Node(3)
# lst.next.next.next = Node(4)
# # lst.next.next.next.next = Node(5)

# print("Original lst:")
# print(stringify(lst))
# reversed_lst = reverse(lst)

# print("\nReversed lst:")
# print(stringify(reversed_lst))