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

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return str(self.val)

class ListHead:
    def __init__(self, node: ListNode=None):
        self.node = node
    
    def __repr__(self):
        res = []
        node = self.node
        while (node != None):
            res += [str(node.val)]
            node = node.next
        res += ['Null']
        return '->'.join(res)

lst = [ListNode(x) for x in [1,2,3,4,5]]
lst[0].next = lst[1]
lst[1].next = lst[2]
lst[2].next = lst[3]
lst[3].next = lst[4]
hd = lst[0]

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
print(f'input:{hd}')
res = ListHead(s.middleNode(lst[0]))
print(f'res:{res}')