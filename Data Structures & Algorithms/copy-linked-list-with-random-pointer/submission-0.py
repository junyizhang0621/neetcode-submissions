"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        hash_table = {None: None}

        copy = head
        while copy:
            copy_node = Node(copy.val)
            hash_table[copy] = copy_node
            copy = copy.next
        
        copy = head

        while copy:
            cur_node = hash_table[copy]
            cur_node.next = hash_table[copy.next]
            cur_node.random = hash_table[copy.random]
            copy = copy.next
        
        return hash_table[head]
            
            
        