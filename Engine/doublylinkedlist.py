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

    def append(self, new_node):
        if not self.head:  # 0 elements
            self.head = new_node
            self.tail = self.head

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, new_node):
        if not self.head:
            self.head = new_node
            self.tail = self.head

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_end(self):
        if not self.head:
            return
        elif not self.head.next:
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

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

    def remove_beginning(self):
        if not self.head:
            return
        elif not self.head.next:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

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


# Tests
# dll = DoublyLinkedList()
# dll.prepend(Node(1))
# dll.prepend(Node(2))
# dll.prepend(Node(3))
# dll.prepend(Node(4))
# dll.prepend(Node(5))
# print(dll.head)

# dll1 = DoublyLinkedList()
# dll1.append(Node(1))
# dll1.append(Node(2))
# dll1.append(Node(3))
# dll1.append(Node(4))
# dll1.append(Node(5))
# print(dll1.head)

# dll2 = DoublyLinkedList()
# dll2.append(Node(1))
# print(dll2.head)
# dll2.prepend(Node(2))
# print(dll2.head)
# dll2.append(Node(3))
# print(dll2.head)
# dll2.append(Node(4))
# print(dll2.head)
# dll2.prepend(Node(5))
# print(dll2.head)
# dll2.remove_beginning()
# print(dll2.head)
# dll2.remove_end()
# print(dll2.head)
# dll2.remove_beginning()
# print(dll2.head)
# dll2.remove_end()
# print(dll2.head)
# dll2.remove_end()
# print(dll2.head)

# dll3 = DoublyLinkedList()

# for i in range(10):  # Fill list
#     if i % 2 == 0:
#         print(f'Appending {i}')
#         dll3.append(Node(i))
#     else:
#         print(f'Prepending {i}')
#         dll3.prepend(Node(i))
    
#     print(dll3)

# for i in range(11):  # Remove from list
#     if i % 2 == 0:
#         print(f'Remove beginning')
#         dll3.remove_beginning()
#     else:
#         print(f'Remove end')
#         dll3.remove_end()

#     print(dll3)

# dll4 = DoublyLinkedList()

# for i in range(10):  # Fill list
#     if i % 2 == 0:
#         print(f'Appending {i}')
#         dll4.append(Node(i))
#     else:
#         print(f'Prepending {i}')
#         dll4.prepend(Node(i))
    
#     print(dll4)

# for i in range(11):  # Remove from list
#     if i % 2 == 0:
#         print(f'Popping beginning has value {dll4.pop_beginning()}')
#     else:
#         print(f'Popping end has value {dll4.pop_end()}')

#     print(dll4)