


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