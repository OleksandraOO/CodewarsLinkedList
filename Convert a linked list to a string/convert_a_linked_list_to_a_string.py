class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node: Node):
    if node is None:
        return "None"
    else:
        return str(node.data) + " -> " + stringify(node.next)
