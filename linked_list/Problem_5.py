# Problem_5.py
# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.

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

def add_reverse(nums1, nums2):
    total = list()
    if nums1.length > nums2.length:
        size = nums1.length
    else:
        size = nums2.length

    while size != 0:
        if nums1.head == None:
            if nums2.head == None:
                size = 0
            else:
                n = nums2.head.data
                nums2.head = nums2.head.next
                total.append(n)
        elif nums2.head == None:
            if nums1.head == None:
                size = 0
            else:
                n = nums1.head.data
                nums1.head = nums1.head.next
                total.append(n)
        else:
            n = nums1.head.data + nums2.head.data
            nums1.head = nums1.head.next
            nums2.head = nums2.head.next
            total.append(n)
        size -= 1

    result = LinkedList()
    carry = 0
    for n in range(0, len(total)):
        if n == 0:
            if total[n] > 9:
                carry = int(total[n]/10)
                total[n] = total[n]%10
                result.add(total[n])
            else:
                result.add(total[n])
        else:
            if total[n] > 9 and carry == 0:
                carry = int(total[n]/10)
                total[n] = total[n]%10
                result.add(total[n])
            elif total[n] > 9:
                ct = carry
                carry = int(total[n]/10)
                total[n] = total[n]%10
                result.add(total[n]+ct)
            else:
                result.add(total[n]+carry)
                carry = 0

    return result

def add(nums1, nums2):
    total = list()
    if nums1.length > nums2.length:
        size = nums1.length
    else:
        size = nums2.length

    while size != 0:
        if nums1.head == None:
            if nums2.head == None:
                size = 0
            else:
                n = nums2.head.data
                nums2.head = nums2.head.next
                total.append(n)
        elif nums2.head == None:
            if nums1.head == None:
                size = 0
            else:
                n = nums1.head.data
                nums1.head = nums1.head.next
                total.append(n)
        else:
            n = nums1.head.data + nums2.head.data
            nums1.head = nums1.head.next
            nums2.head = nums2.head.next
            total.append(n)
        size -= 1
    total.reverse()
    t = list()
    carry = 0
    for n in range(0, len(total)):
        if n == 0:
            if total[n] > 9:
                carry = int(total[n]/10)
                total[n] = total[n]%10
                t.append(total[n])
            else:
                t.append(total[n])
        else:
            if total[n] > 9 and carry == 0:
                carry = int(total[n]/10)
                total[n] = total[n]%10
                t.append(total[n])
            elif total[n] > 9:
                ct = carry
                carry = int(total[n]/10)
                total[n] = total[n]%10
                t.append(total[n]+ct)
            else:
                t.append(total[n]+carry)
                carry = 0
    result = LinkedList()
    t.reverse()
    for n in t:
        result.add(n)

    return result
def main():
    numbers1 = [2,7,1,6]
    numbers2 = [5,9,2]
    links_1 = LinkedList()
    links_2 = LinkedList()
    for n in numbers1:
        links_1.add(n)

    for n in numbers2:
        links_2.add(n)

    print("Linked list 1: {} and linked list 2: {}".format(links_1.print(), links_2.print()))
    results = add_reverse(links_1, links_2)
    print("Sum list results: {}".format(results.print()))

    numbers1 = [6,1,7,2]
    numbers2 = [2,9,5]
    links_1 = LinkedList()
    links_2 = LinkedList()
    for n in numbers1:
        links_1.add(n)

    for n in numbers2:
        links_2.add(n)

    print("Linked list 1: {} and linked list 2: {}".format(links_1.print(), links_2.print()))
    results = add(links_1, links_2)
    print("Sum list results: {}".format(results.print()))

main()