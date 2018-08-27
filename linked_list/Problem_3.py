# Problem_3.py
# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        elif self.tail is None:
            self.tail = node
            self.head.next = self.tail
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def pop(self):
        node = self.head
        self.head = self.head.next
        self.length -= 1
        return node

    def delete_selected(self, data):
        current = self.head
        while current.data != data:
            current = current.next
        if current == None or current.next == None:
            return False

        node = current.next
        current.data = node.data
        current.next = node.next
        return True

    def print(self):
        current = self.head
        string = ''
        while current != None:
            string += str(current.data) + ", "
            current = current.next
        return string[:-2]

links = LinkedList()

def main():
    test_data = ['a', 'b', 'c', 'd', 'e', 'f']
    for n in test_data:
        links.add(n)
    result = links.delete_selected('c')

    print("result: {} \t linked list: {}".format(result, links.print()))
main()
