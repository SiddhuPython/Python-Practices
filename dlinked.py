class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
class DoubleLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
    def get_node(self, index):
        current = self.first
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current
    def insert_at_beg(self, new_node):
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.insert_before(self.first, new_node)
    def insert_before(self, ref_node, new_node):
        new_node.next = ref_node
        if ref_node.prev is None:
            self.first = new_node
        else:
            new_node.prev = ref_node.prev
            new_node.prev.next = new_node
        ref_node.prev = new_node
    def display(self):
        current = self.first
        while current:
            print(current.data)
            current = current.next

if __name__ == "__main__":
    data = 10
    new_node = Node(data)
    dl = DoubleLinkedList()
    print(dl.get_node(0))
    dl.insert_at_beg(new_node)
    print(dl.display())
        
    