from linklist import Linkedlist

r = Linkedlist()
a = [1,2,3,4,5,6,7]
[r.insert(i) for i in a]
r.traverse_ll()

# Time Complexity: O(N) and Space: O(1)
# Floydd Cycle detection algorithm

def startOfCycle(r):
    fast = slow = r.getHead()
    while fast and fast.nextNode:
        slow, fast = slow.nextNode, fast.nextNode.nextNode
        if fast == slow:
            break
    else:   # if not fast and fast.next return None
        return None
    
    pointer = r.getHead()
    while fast != pointer:
        fast, pointer = fast.nextNode, pointer.nextNode
    return pointer.data

r.head.nextNode.nextNode.nextNode.nextNode.nextNode = r.head.nextNode.nextNode
print(startOfCycle(r))