# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        for i in range(1, len(lists)):
            l1 = lists[i-1]
            l2 = lists[i]

            lists[i] = self.mergeLists(l1, l2)
        
        return lists[-1]

        
    def mergeLists(self, l1, l2):
        dummy = head = ListNode()

        while l1 and l2:
            v1 = l1.val
            v2 = l2.val

            if v1 <= v2:
                head.next = l1
                head = head.next
                l1 = l1.next
            else:
                head.next = l2
                head = head.next
                l2 = l2.next
        
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        
        return dummy.next



        
        