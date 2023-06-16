from linklist import e, Node

a = [1,2,3,4,5]
[e.insert(i) for i in a]
e.traverse_ll()

def reverseKGroup(e, k):
    dummy = Node(0)
    dummy.nextNode = e.getHead()
    groupPrev = dummy

    while True:
        kth = getKth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.nextNode

        # reverse group
        prev, curr = kth.nextNode ,groupPrev.nextNode

        while curr != groupNext:
            temp = curr.nextNode
            curr.nextNode = prev
            prev = curr
            curr = temp
        
        temp = groupPrev.nextNode
        groupPrev.nextNode = kth
        groupPrev = temp

    return dummy.nextNode




def getKth(curr, k):
    while curr and k > 0:
        curr = curr.nextNode
        k -= 1
    return curr

reverseKGroup(e,2)
e.traverse_ll()