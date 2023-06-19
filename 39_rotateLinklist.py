from linklist import Linkedlist

x = Linkedlist()
a = [1,2,3,4,5]
[x.insert(i) for i in a]

def rotateList(x, k):
    h = x.getHead()
    if not h:
        return h

    # get length
    length, t = 1, x.getTail()
    while t.nextNode:
        t = t.nextNode
        length += 1
    
    k = k % length
    if k == 0:
        return h
    
    # move to pivot and rotate
    curr = h
    for i in range(length - k - 1):
        curr = curr.nextNode
    newHead = curr.nextNode
    curr.nextNode = None
    t.nextNode = h
    return newHead


print(rotateList(x, 2))
x.traverse_ll()


