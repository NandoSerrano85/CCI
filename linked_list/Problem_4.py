# Problem_4.py
# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.

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
def partition(links, data):
    before = LinkedList()
    after = LinkedList()
    current = links.head
    while current != None:
        if current.data < data:
            before.add(current.data)
        else:
            after.add(current.data)
        current = current.next

    result = LinkedList()
    while before.head != None:
        result.add(before.head.data)
        before.head = before.head.next

    while after.head != None:
        result.add(after.head.data)
        after.head = after.head.next
    return result

def main():
    tester = [3,5,8,5,10,2,1]
    k = 8
    links = LinkedList()
    for n in tester:
        links.add(n)

    results = partition(links, k)

    print("With partition: {} the result is {}".format(k, results.print()))
main()

