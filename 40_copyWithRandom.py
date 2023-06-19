# two pass algorithm using hashmap
# Time : O(N) and Space : O(N)

def copyRandomList(head):
    oldToCopy = {None : None}

    curr = head
    while curr:
        copy = Node(curr.data)
        oldToCopy[curr] = copy
        curr = curr.nextNode

    curr = head
    while curr:
        copy = oldToCopy[curr]
        copy.next = oldToCopy[curr.next]
        copy.random = oldToCopy[curr.random]
        curr = curr.next
                                
    return oldToCopy[head]