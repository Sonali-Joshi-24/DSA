from linklist import Node, s

a = [1,2,3,4,5]
[s.insert(i) for i in a]
s.traverse_ll()

def removeNthFromEnd(s, n):
    dummy = Node(0)
    dummy.nextNode = s.getHead()
    
    left = dummy
    right = s.getHead()

    while n > 0 and right:
        right = right.nextNode
        n -= 1
    
    
    while right:
        left = left.nextNode
        right = right.nextNode
    
    left.nextNode = left.nextNode.nextNode
    return dummy.nextNode


removeNthFromEnd(s,2)
s.traverse_ll()
