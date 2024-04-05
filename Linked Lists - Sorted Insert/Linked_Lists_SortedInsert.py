class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    if data < head.data:
        new_node.next = head
        return new_node
    new_list = head
    while new_list.next is not None and new_list.next.data < data:
        new_list = new_list.next
    new_node.next = new_list.next
    new_list.next = new_node
    return head
