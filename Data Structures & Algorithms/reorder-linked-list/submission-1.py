# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        # Getting middle of list
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reversing second half
        cur2, prev2, slow.next = slow.next, None, None
        while cur2:
            tmp = cur2.next
            cur2.next = prev2
            prev2 = cur2
            cur2 = tmp
        # Merging the two halves
        cur1, cur2 = head, prev2
        while cur2:
            tmp1, tmp2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = tmp1
            cur1, cur2 = tmp1, tmp2
            
            
            
        
        