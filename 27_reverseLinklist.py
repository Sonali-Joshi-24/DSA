from linklist import r

a = [1,2,3,4,5,6,7]
[r.insert(i) for i in a]

r.traverse_ll()

def reverse_linklist(r):
    current_node = r.getHead()
    prev_node = None

    while current_node is not None:
        next_pointer = current_node.nextNode
        current_node.nextNode = prev_node
        prev_node = current_node
        current_node = next_pointer
    r.head = prev_node

reverse_linklist(r)
r.traverse_ll()
