# O(N) time and O(1) space
from linklist import Node, p, q

a = [10,20,30,40]
[p.insert(i) for i in a]
p.traverse_ll()

b = [5,15,25,35]
[q.insert(i) for i in b]
q.traverse_ll()


def merge_sorted_linklist(p,q):
    if not p:
        q.traverse_ll()
        return
    if not q:
        p.traverse_ll()
        return
    
    # initiliazing pointers at begining of both list
    h1 = p.getHead()
    h2 = q.getHead()
    h = dummy = Node(0)   # a dummy node takes up constant space O(1)... dummy node representation will be 0=>5=>10... etc


    while h1 and h2:
        if h1.data < h2.data:
            h.nextNode = h1
            h1 = h1.nextNode
        else:
            h.nextNode = h2
            h2 = h2.nextNode
        
        h = h.nextNode
    
    # check the base case if any list is still non - empty
    if h1: h.nextNode = h1
    if h2: h.nextNode = h2

    return dummy.nextNode    #since dummy node carrys 0 so we return dummy.nextnode

print('------------linklist after merging----------------')
merge_sorted_linklist(p,q)
p.traverse_ll()