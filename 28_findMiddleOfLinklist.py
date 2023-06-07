from linklist import m

r = [1,2,3,4,5,6]
r = ['a','b','c','d','e']
[m.insert(i) for i in r]
m.traverse_ll()

def find_middle_of_linklist(m):
    p = m.getHead()
    q = m.getHead()

    while q and q.nextNode:
        p = p.nextNode
        q = q.nextNode.nextNode
    return p.data

print(find_middle_of_linklist(m))

