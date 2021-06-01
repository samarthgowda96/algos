class Solution:
    def mergeTwoLinkedList(Self,l1,l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        elif l1.val <l2.val:
            l1.next= self.mergeTwoLinkedList(l1.next,l2)
            return l1
        else:
            l2.next= self.mergeTwoLinkedList(l1,l2.next)
            return l2