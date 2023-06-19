class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

        self.no_of_nodes = 0

    def insert(self, data):
        self.no_of_nodes += 1
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.nextNode = newNode
            self.tail = newNode
    
    # problem 2: insert at the end of linklist
    def insert_at_end(self,data):
        self.no_of_nodes += 1

        newNode = Node(data)
        if self.head is None:
            return newNode.data
        else:
            self.tail.nextNode = newNode
            self.tail = newNode
    
    # insert at the end of linklist
    def insert_at_begining(self,data):
        self.no_of_nodes += 1

        newNode = Node(data)
        if self.head == None:
            return newNode.data
        else:
            newNode.nextNode = self.head
            self.head = newNode

    # insert at specific location
    def insert_at_specific_location(self,node,data):
        self.no_of_nodes += 1

        newNode = Node(data)
        if node is None:
            return
        else:
            newNode.nextNode = node.nextNode
            node.nextNode = newNode

    # display the linklist
    def traverse_ll(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="==>")
            temp = temp.nextNode
        print('Null')

    
    # delete 
    def delete(self,position):
        self.no_of_nodes -= 1

        temp = self.head
        if self.head == 0:
            return
        if position == 0:
            self.head = temp.nextNode
            temp = None

        for i in range(position - 1):
            temp = self.head
            if temp is None:
                break
        if temp is None:
            return
        if temp.nextNode is None:
            return
        
        newConn = temp.nextNode.nextNode
        temp.nextNode = None
        temp.nextNode = newConn
    

    def getHead(self):
        return self.head
    
    def getTail(self):
        return self.tail

    def size_of_list(self):
        return self.no_of_nodes


l = Linkedlist()
r = Linkedlist()   #for reverse a linklist
m = Linkedlist()  #for middle of linklist

# merge 2 sorted linklist
p = Linkedlist()
q = Linkedlist()

# removeNth node from back
s = Linkedlist()

# add two numbers ll
a = Linkedlist()
b = Linkedlist()


# delete a node when it is given
d = Linkedlist()


# intersection in ll
i = Linkedlist()
j = Linkedlist()


# linklist cycle
z = Linkedlist()

# reverse ll k ele
e = Linkedlist()


# a = [10,20,30,40]
# [l.insert(i) for i in a]
# l.traverse_ll()
# print(l.size_of_list())

# l.delete(1)
# l.traverse_ll()
# print(l.size_of_list())

