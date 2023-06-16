from linklist import i, j

a = [4,1,8,4,5]
[i.insert(x) for x in a]
i.traverse_ll()

b = [5,6,7,8,4,5]
[j.insert(y) for y in b]
j.traverse_ll()


def getIntersectionNode(i,j):
    p1, p2 = i.getHead(), j.getHead()
    l1, l2 = i.size_of_list(), j.size_of_list()

    if p1.data == p2.data:
        return None
    if l1 > l2:
        for _ in range(l1-l2):
            p1 = p1.nextNode
    if l2 > l1:
        for _ in range(l2-l1):
            p2 = p2.nextNode

    while p1 and p2:
        if p1.data == p2.data:
            return p1.data
        
        p1 = p1.nextNode
        p2 = p2.nextNode



print(getIntersectionNode(i,j))