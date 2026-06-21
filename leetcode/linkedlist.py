class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

head = ListNode(0)
res = head

while l1 or l2:
    sum = l1.val + l2.val
    
    res.next = ListNode(sum)
    res = res.next

    l1 = l1.next
    l2 = l2.next

print(head.next)