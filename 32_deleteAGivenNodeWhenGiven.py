from linklist import d

a =[4,5,1,9]
[d.insert(i) for i in a]
d.traverse_ll()



def deleteNode(n):
    n.data = n.nextNode.data
    n.nextNode = n.nextNode.nextNode
