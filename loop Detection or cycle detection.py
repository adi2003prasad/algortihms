
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#  also known as floyds cycle detection algorithm.. or hare and rabbit method
class Solution:
    # concept of slow and fast pointer
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        def recFind(head):
            fast = head
            # here we create two identical lists and see if one repeats the other
            try:
                while(fast.next.next and head.next):
                    head = head.next # this one moves one at a time
                    fast = fast.next.next # this one moves two at a time 
                    # so after some time the later will reach the same start point as the first eventually reporting a loop
                    
                    if(head is fast):return True
            except:
                return False
        return recFind(head)