

from linklist import z

a = [1,2,3,4,5]
[z.insert(i) for i in a]

def detectCycle(z):
    if not z:
        return
    
    fast = z.getHead()
    slow = z.getHead()

    while fast and slow and fast.nextNode:
        slow = slow.nextNode
        fast = fast.nextNode.nextNode

        if fast == slow:
            return True
    return False


# I want 5 to point to 2 (created a cycle)
z.head.nextNode.nextNode.nextNode.nextNode = z.head.nextNode
print(detectCycle(z))
