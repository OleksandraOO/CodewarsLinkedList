class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source: Node, dest: Context):
    if source is None:
        raise Exception
    else:
        new = source.next
        source.next = dest
        return Context(new, source)
