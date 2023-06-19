'''
Input:
5 -> 10 -> 19 -> 28
|     |     |     | 
7     20    22   35
|           |     | 
8          50    40
|                 | 
30
Output:  5-> 7-> 8- > 10 -> 19-> 20->22-> 28-> 30-> 35-> 40-> 45-> 50.
Explanation:
The resultant linked lists has every 
node in a single level.
(Note: | represents the bottom pointer.)
'''
# only code is written for reference

'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

def flatten(root):
    #Your code here
    if root is None or root.next is None:
        return root
        
    # recursion for list on right
    root.next = flatten(root.next)
    # merge the list
    root = mergeTwoList(root, root.next)
    return root
    
def mergeTwoList(a,b):
    dummy = Node(0)
    res = dummy
    
    while a and b:
        if a.data < b.data:
            dummy.bottom = a
            dummy = dummy.bottom
            a = a.bottom
        else:
            dummy.bottom = b
            dummy = dummy.bottom
            b = b.bottom
            
    if a:
        dummy.bottom = a
    if b:
        dummy.bottom = b
    return res.bottom



