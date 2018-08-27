# Problem_2.py
# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

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
            string += str(current.data) + ", "
            current = current.next
        return string[:-2]

def kth_to_last(links, k):
    output = links
    if output.head.next is None:
        return output
    elif output.length < k:
        return 'exceds the length of the linked list'
    else:
        for n in range(0, k):
            output.head = output.head.next
        return output

def main():
    links = LinkedList()
    k = 20
    test_input = [1,1,1,2,3,4,5,2,3,4,8,23,12,2213,2200,343]
    for n in test_input:
        links.add(n)

    results = kth_to_last(links, k)
    if isinstance(results, str):
        print("Error: k of {} requested {}".format(k, results))
    else: 
        print('{}th to last node is {}'.format(k, results.print()))

main()