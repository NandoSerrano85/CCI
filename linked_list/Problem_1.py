# Problem_1.py
# 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

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

    def print(self):
        current = self.head
        string = ''
        while current != None:
            string += str(current.data) + " => "
            current = current.next
        print(string[:-2])

def remove_dups(links):
    clean = list()
    size = links.length
    while size != 0:
        node = links.pop()
        if node.data in clean:
            pass
        else:
            clean.append(node.data)
        size -= 1
        
    results = LinkedList()
    for n in clean:
        results.add(n)
    return results

def main():
    links = LinkedList()
    test_input = [1,1,1,2,3,4,5,2,3,4,8,23,12,2213,2200,343]
    for n in test_input:
        links.add(n)

    print("original linked list:")
    links.print()
    unique = remove_dups(links)
    print("\nafter removing duplicates:")
    unique.print()

main()
