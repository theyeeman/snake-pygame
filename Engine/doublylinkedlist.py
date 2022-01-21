from email import header


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

    def to_list(self):
        curr = self.head
        ret = []

        while curr:
            ret.append(curr.val)
            curr = curr.next

        return ret



# Tests
# dll = DoublyLinkedList()
# dll.prepend(1)
# dll.prepend(2)
# dll.prepend(3)
# dll.prepend(4)
# dll.prepend(5)
# print(dll.head)
# print(dll.to_list())

# dll1 = DoublyLinkedList()
# dll1.append(1)
# dll1.append(2)
# dll1.append(3)
# dll1.append(4)
# dll1.append(5)
# print(dll1.head)

# dll2 = DoublyLinkedList()
# dll2.append(1)
# print(dll2.head)
# dll2.prepend(2)
# print(dll2.head)
# dll2.append(3)
# print(dll2.head)
# dll2.append(4)
# print(dll2.head)
# dll2.prepend(5)
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

## test remove
# dll3 = DoublyLinkedList()

# for i in range(10):  # Fill list
#     if i % 2 == 0:
#         print(f'Appending {i}')
#         dll3.append(i)
#     else:
#         print(f'Prepending {i}')
#         dll3.prepend(i)
    
#     print(dll3)

# for i in range(11):  # Remove from list
#     if i % 2 == 0:
#         print(f'Remove beginning')
#         dll3.remove_beginning()
#     else:
#         print(f'Remove end')
#         dll3.remove_end()

#     print(dll3)

# test pop
# dll4 = DoublyLinkedList()

# for i in range(10):  # Fill list
#     if i % 2 == 0:
#         print(f'Appending {i}')
#         dll4.append(i)
#     else:
#         print(f'Prepending {i}')
#         dll4.prepend(i)
    
#     print(dll4)

# for i in range(11):  # Remove from list
#     if i % 2 == 0:
#         print(f'Popping beginning has value {dll4.pop_beginning()}')
#     else:
#         print(f'Popping end has value {dll4.pop_end()}')

#     print(dll4)

# test peek
# dll5 = DoublyLinkedList()

# for i in range(10):  # Fill list
#     if i % 2 == 0:
#         dll5.append(i)
#     else:
#         dll5.prepend(i)
    
#     print(dll5)
#     print(f'peek beginning {dll5.peek_beginning()}, peek end {dll5.peek_end()}\n')