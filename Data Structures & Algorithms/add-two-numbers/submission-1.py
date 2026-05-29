# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode()
        additional = 0
        while l1 and l2:
            cur_num = l1.val + l2.val + additional
            digit = cur_num % 10
            additional = cur_num // 10

            head.next = ListNode(digit)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            cur_num = l1.val + additional
            digit = cur_num % 10
            additional = cur_num // 10

            head.next = ListNode(digit)
            head = head.next
            l1 = l1.next
        
        while l2:
            cur_num = l2.val + additional
            digit = cur_num % 10
            additional = cur_num // 10

            head.next = ListNode(digit)
            head = head.next
            l2 = l2.next

        if additional != 0:
            head.next = ListNode(additional)
        
        return dummy.next

