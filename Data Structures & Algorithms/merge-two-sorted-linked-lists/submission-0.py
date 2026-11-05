# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = list1, list2
        dummy = ListNode()
        h3 = dummy
        while h1 is not None and h2 is not None:
            if h1.val < h2.val:
                h3.next = h1
                h1 = h1.next
            else:
                h3.next = h2
                h2 = h2.next
            h3 = h3.next

        if h1 is not None:
            h3.next = h1
        else:
            h3.next = h2
        return dummy.next


        