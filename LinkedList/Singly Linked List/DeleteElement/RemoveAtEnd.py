class Node:
    def __init__(self, data):
        self.data = data
        self.reference = None


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if (self.head is None):
            print('Linked List is Empty!')
        else:
            n = self.head
            while (n is not None):
                print(n.data, '-->', end=' ')
                n = n.reference

    def atBeginning(self, data):
        new_node = Node(data)
        new_node.reference = self.head
        self.head = new_node

    def atEnd(self, data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
        else:
            n = self.head
            while (n.reference is not None):
                n = n.reference
            n.reference = new_node

    def add_after_given_node(self, data, x):
        n = self.head
        while (n is not None):
            if (x == n.data):
                break
            n = n.reference
        if (n is None):
            print('Node is not present in the given Linked List')
        else:
            new_node = Node(data)
            new_node.reference = n.reference
            n.reference = new_node

    def add_before_given_node(self, data, x):
        if (self.head == None):
            print("Linked list is empty!")
            return
        if (self.head.data == x):
            new_node = Node(data)
            new_node.reference = self.head
            self.head = new_node
            return
        n = self.head
        while(n.reference is not None):
            if (n.reference.data == x):
                break
            n = n.reference
        if (n.reference is None):
            print('Node not found')
        else:
            new_node = Node(data)
            new_node.reference = n.reference
            n.reference = new_node

    def delete_beginning(self):
        if(self.head is None):
            print('LinkedList is empty we can not delete nodes!')
        else:
            self.head = self.head.reference
    def delete_end(self):
        if(self.head is None):
            print('LinkedList is empty we can not delete nodes!')
        elif (self.head.reference is None):
            self.head = None
        else:
            n = self.head
            while (n.reference.reference is not None):
                n = n.reference 
            n.reference = None


LL1 = LinkedList()
LL1.atBeginning(10)
LL1.atEnd(20)
LL1.atEnd(30)
LL1.delete_end()
LL1.isEmpty()