'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

'''
from typing import Optional
from typing import List
from xml.dom.minicompat import NodeList

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return str(self.val)

class LinkedList:
    def __init__(self, list: List[int]):
        self.head = LinkedList.buildList(list)

    @staticmethod
    def buildList(list: List[int]) -> ListNode:
        head = None
        tail = ListNode()
        for x in list:
            tail.next = ListNode(x, None)
            tail = tail.next
            if (head == None):
                head = tail
        return head

    @staticmethod
    def printList(head):
        res = []
        node = head
        while (node != None):
            res += [str(node.val)]
            node = node.next
        res += ['Null']
        return '->'.join(res)
   
    def __str__(self) -> str:
        return LinkedList.printList(self.head)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        Dummy = ListNode(0, head)
        l = Dummy
        r = head
        while (n > 0 and r != None):
            r = r.next
            n -= 1
        while (r != None):
            l = l.next
            r = r.next
        l.next = l.next.next
        return Dummy.next


n = 1
lst = LinkedList([1,2,3,4,5])
print(f'input:{lst} n:{n}')

s = Solution()
res = s.removeNthFromEnd(lst.head, n)
print(f'res:{LinkedList.printList(res)}')
