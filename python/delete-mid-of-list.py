'''
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 

Example 1:


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
Example 2:


Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
'''

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, init: List[int]) -> None:
        tail = ListNode()
        self.head = tail 
        for x in init:
            tail.next = ListNode(x, None)
            tail = tail.next
        self.head = self.head.next

    @staticmethod
    def printList(head: ListNode) -> str:
        res = []
        while (head != None):
            res += [str(head.val)]
            head = head.next
        res += ['None']
        return '->'.join(res)
    
    def __repr__(self) -> str:
        return LinkedList.printList(self.head)

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Zero = ListNode(0, head)
        mid = Zero
        end = head
        shift_mid = True

        while (end.next != None):
            end = end.next
            if (shift_mid):
                mid = mid.next
            shift_mid = not shift_mid
        mid.next = mid.next.next
        return Zero.next

inp = LinkedList([1])
print(f'input:{inp}')
s = Solution()
res = s.deleteMiddle(inp.head)
print(f'res:{LinkedList.printList(res)}')
        


