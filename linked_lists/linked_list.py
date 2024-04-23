class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_in_list(self, data, index):
        if self.head is None:
            self.insert_at_beginning(data)
        else:
            itr = self.head
            flag = 0
            while itr:
                if flag == index - 1:
                    temp = Node(data, itr.next)
                    temp.next = itr.next
                    itr.next = temp
                    break
                flag = flag + 1
                itr = itr.next

    def insert_after_value(self, data, value):
        if self.head is None:
            raise Exception("No data to be searched")
        else:
            itr = self.head
            count = 0
            while itr:
                if itr.data == value:
                    temp = Node(data, itr.next)
                    itr.next = temp
                    break
                count += 1
                itr = itr.next

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None)

    def remove_from_list(self, index):
        if self.head is None or index < 0:
            print("no element to remove from the list --- >")
        elif index == 0:
            self.head = self.head.next
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    break

                itr = itr.next
                count = count + 1

    def remove_by_value(self, data):
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def traverse_list(self):
        itr = self.head
        while itr:
            print("data---->", itr.data, end=" ")
            itr = itr.next


l1 = LinkedList()
l1.insert_at_beginning(2)
l1.insert_at_end(212)
l1.insert_at_end(12)

l1.insert_in_list(10, 1)
l1.insert_in_list(11110, 3)
# l1.insert_at_end(56)
# l1.insert_after_value(200, 2)

l1.traverse_list()
