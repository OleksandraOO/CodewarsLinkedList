class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    # def __eq__(self, value: object) -> bool:
    #     return self.data == value.data
    def __repr__(self) -> str:
        return f'({self.data}, {self.next})'


def remove_duplicates(head):
    if head is None or head.next is None:
        return head

    for i in range(10):
        temp = head
        while temp is not None and temp.next is not None:
            # one = temp.data
            # two = temp.next.data
            if temp.data == temp.next.data:
                temp.next = temp.next.next
            temp = temp.next
    return head


def stringify(node: Node):
    if node is None:
        return "None"
    else:
        return str(node.data) + " -> " + stringify(node.next)


# lst = Node(1)
# lst.next = Node(1)
# lst.next.next = Node(1)
# lst.next.next.next = Node(1)
# lst.next.next.next.next = Node(1)

# print("Original lst:")
# print(stringify(lst))
# remove_duplicates = remove_duplicates(lst)

# print("\nReversed lst:")
# print(stringify(remove_duplicates))