# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverse(self, l2):
        prev = None
        curr = l2
        while curr:
            nextN = curr.next
            curr.next = prev
            prev = curr 
            curr = nextN
        return prev


    def reorderList(self, head: Optional[ListNode]) -> None:

        slow= head 
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next 

        l1 = head 
        l2 = slow.next 
        slow.next = None 
        l2_rev = self.reverse(l2)

        # merge 

        while l1 and l2_rev:

            un = l1.next 
            dn = l2_rev.next 

            l1.next = l2_rev
            l2_rev.next = un 

            l1 = un 
            l2_rev = dn 
        









        