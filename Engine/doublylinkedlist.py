class Node():
    def __init__(self, val=None):
        self.prev = None
        self.next = None
        self.val = val

    def __str__(self):
        curr = self
        stack = []
        while curr:
            stack.append(str(curr.val))
            curr = curr.next

        return ' '.join(stack)


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return str(self.head)

    def append(self, val):
        new_node = Node(val)

        if not self.head:  # 0 elements
            self.head = new_node
            self.tail = self.head

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            self.tail = self.head

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_end(self):
        self.pop_end()

    def pop_end(self):
        if not self.head:
            return None

        ret = self.tail.val

        if not self.head.next:
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return ret

    def peek_end(self):
        if not self.tail:
            return None

        return self.tail.val

    def remove_beginning(self):
        self.pop_beginning()

    def pop_beginning(self):
        if not self.head:
            return None

        ret = self.head.val

        if not self.head.next:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

        return ret

    def peek_beginning(self):
        if not self.head:
            return None

        return self.head.val

    def to_list_full(self):
        return self.to_list_from_node(self.head)

    def to_list_from_node(self, curr):
        ret = []

        while curr:
            ret.append(curr.val)
            curr = curr.next

        return ret
