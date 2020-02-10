class Node(object):
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        """Insert a new node at the end of the linked list"""
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data)

    def prepend(self, data):
        """Insert node at the beginning of the linked list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        """Insert a new node in the middle of the linked list"""
        if not prev_node:
            print("Previous node is not in the linked list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

ll = LinkedList()
ll.append('jf')

ll.print_list()