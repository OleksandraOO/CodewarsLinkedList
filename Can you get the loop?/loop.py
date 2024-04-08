def loop_size(node):
    first = node
    second = node.next
    while first != second:
        first = first.next
        second = second.next.next
    result = 1
    first = first.next
    while first != second:
        first = first.next
        result += 1
    return result
