# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        start = ListNode()
        start.next = head
        current = start
        while current.next and current.next.next:
            tmp = current.next # Save 1st Node
            current.next = current.next.next #Place 2nd Node
            tmp.next = current.next.next # Update 1st Node
            current.next.next = tmp # Update 2nd Node (Place 1st Node)
            current = current.next.next # Step
        return start.next
            

        