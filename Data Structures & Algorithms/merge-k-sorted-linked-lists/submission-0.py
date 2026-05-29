# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            lastest_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                lastest_list.append(self.mergeLists(l1, l2))
            lists= lastest_list
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



        
        