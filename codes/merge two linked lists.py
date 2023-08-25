class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        a = list1.val
        b = list2.val
        if a<b:
            return ListNode(a, self.mergeTwoLists(list1.next, list2))
        else:
            return ListNode(b, self.mergeTwoLists(list1, list2.next))
        