
def create_nodes(lis):
    e = Node(lis[0])
    head = e
    for i in lis[1:]:
        e1 = Node(i)
        e.next = e1
        e = e1
    return head

cases = [[1], [1,2], [1,2,2,1], [1,2,3,2,1], [1,1,2,1], [1,0,1,1]]
for c in cases:
    head = create_nodes(c)
    s.isPalindrome(head)
