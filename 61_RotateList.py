# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        ##Edge Cases
        if not head or not head.next or k == 0:
            return head


        ## Get Tail and Length
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        ##Normalise k
        k = k % length
        if k == 0:
            return head

        ##Make circular
        tail.next = head



        ##Find New head and tail
        steps = length - k - 1
        new_tail = head
        for _ in range(steps):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head

        