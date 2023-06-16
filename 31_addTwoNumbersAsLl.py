'''
2 --> 4 --> 3  = l1
5 --> 6 --> 4  = l2

output : 342 + 465 = 807
output = 7 --> 0 --> 8

'''


from linklist import a, b, Node

num1 = [9,9,9,9,9,9,9]
[a.insert(i) for i in num1]
a.traverse_ll()

num2 = [9,9,9,9]
[b.insert(i) for i in num2]
b.traverse_ll()




def addTwoNumbers(a,b):
    dummy = Node(0)
    curr = dummy

    carry = 0
    h1 = a.getHead()
    h2 = b.getHead()


    while h1 or h2 or carry:
        # get the values
        v1 = h1.data if h1 else 0
        v2 = h2.data if h2 else 0

        # new digit
        val = v1 + v2 + carry
        # if our no computed is 15 (we want carry out of that)
        carry = val // 10
        # and we want only 1's place digit in val (if 15 then 5)
        val = val % 10
        curr.nextNode = Node(val)

        # update pointer
        curr = curr.nextNode
        h1 = h1.nextNode if h1 else None
        h2 = h2.nextNode if h2 else None


    while dummy.nextNode:
        print(dummy.nextNode.data, end="==>")
        dummy = dummy.nextNode
    print('Null')

print(addTwoNumbers(a,b))





