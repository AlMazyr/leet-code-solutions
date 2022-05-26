'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
'''

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return str(self.val)

class LinkedList:
    def __init__(self, list: List[int]):
        tail = ListNode()
        self.head = tail
        for x in list:
            tail.next = ListNode(x, None)
            tail = tail.next
        self.head = self.head.next
    
    @staticmethod
    def printList(head: ListNode):
        res = []
        node = head
        while (node != None):
            res += [str(node.val)]
            node = node.next
        res += ['Null']
        return '->'.join(res)

    def __repr__(self):
        return LinkedList.printList(self.head)

list = LinkedList([1])
print(f'input:{list}')

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        end = head
        endidx = 0
        mid = end
        while (end.next != None):
            if ((endidx % 2) == 0):
                mid = mid.next
            end = end.next
            endidx += 1
        return mid

s = Solution()
res = s.middleNode(list.head)
print(f'res:{LinkedList.printList(res)}')