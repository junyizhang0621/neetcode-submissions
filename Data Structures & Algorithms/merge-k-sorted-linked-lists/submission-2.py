# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) ==0 :
            return None
        
        if len(lists) ==1 :
            return lists[0]
        
        for i in range(1, len(lists)):
            l1, l2 = lists[i- 1], lists[i]
            lists[i] = self.mergeList(l1, l2)
        
        return lists[-1]
        
    
    def mergeList(self, l1, l2):

        dummmy = head = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                head = head.next
                l1 = l1.next
            else:
                head.next = l2
                head = head.next
                l2 = l2.next
        
        if l1:
            head.next = l1
            l1 = l1.next
            head = head.next
        
        if l2:
            head.next = l2
            l2 = l2.next
            head = head.next
        
        return dummmy.next
        